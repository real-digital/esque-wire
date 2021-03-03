import subprocess

import pytest
from _pytest.fixtures import SubRequest

from tests.cluster_fixture import Cluster, KafkaVersion, SaslEndpoint, SaslSslEndpoint, SslEndpoint
from tests.cluster_fixture.kafka import Endpoint, PlaintextEndpoint

TESTED_KAFKA_VERSIONS = ["1.1.1", "2.0.0", "2.1.0", "2.2.0", "2.3.0", "2.4.0"]


@pytest.fixture(params=TESTED_KAFKA_VERSIONS, ids=[f"kafka_{v.replace('.', '_')}" for v in TESTED_KAFKA_VERSIONS])
def kafka_version(request: SubRequest) -> KafkaVersion:
    return KafkaVersion(request.param)


@pytest.mark.parametrize(
    argnames=["endpoint", "auth_required"],
    argvalues=[
        [PlaintextEndpoint(), False],
        [SaslEndpoint(), False],
        [SaslSslEndpoint(), False],
        [SslEndpoint(), False],
        [SaslSslEndpoint(), True],
        [SslEndpoint(), True],
    ],
    ids=(lambda x: x.security_protocol if isinstance(x, Endpoint) else ["no_ssl_auth", "ssl_auth"][x]),
)
def test_simple_startup(kafka_version: KafkaVersion, endpoint: Endpoint, auth_required: bool) -> None:
    with Cluster(
        kafka_version=kafka_version, endpoints=[endpoint], ssl_client_auth_enabled=auth_required, cluster_size=2
    ) as cluster:
        args = ["/usr/bin/kafkacat", "-L", "-b", ",".join(cluster.get_bootstrap_servers(endpoint.listener_name))]

        if endpoint.ssl_enabled:
            security_protocol = "SSL"
            args += [
                "-X",
                f"ssl.ca.location={cluster.ssl_server_cert_location}",
                "-X",
                f"ssl.keystore.location={cluster.ssl_server_keystore_location}",
                "-X",
                f"ssl.keystore.password={cluster.ssl_store_passphrase}",
            ]
        else:
            security_protocol = "PLAINTEXT"

        if endpoint.sasl_enabled:
            security_protocol = f"SASL_{security_protocol}"
            args += ["-X", "sasl.mechanism=PLAIN", "-X", "sasl.username=admin", "-X", "sasl.password=admin-secret"]

        args += ["-X", f"security.protocol={security_protocol}"]
        subprocess.check_call(args, stdout=subprocess.DEVNULL)
