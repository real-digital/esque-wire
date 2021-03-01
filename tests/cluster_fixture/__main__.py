"""
Just a pytest-agnostic test script for the :class:`Cluster` class.
"""
import logging
import subprocess
import sys
import time
from typing import List

from tests.cluster_fixture import Cluster, KafkaVersion, SaslMechanism, SslEndpoint
from tests.cluster_fixture.kafka import Endpoint

logger = logging.getLogger(__name__)


def main() -> None:
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    sasl_mechanisms: List[SaslMechanism] = []
    endpoints: List[Endpoint] = [SslEndpoint()]
    kafka_version = KafkaVersion("2.1.0")
    with Cluster(
        cluster_size=2,
        endpoints=endpoints,
        sasl_mechanisms=sasl_mechanisms,
        kafka_version=kafka_version,
        ssl_client_auth_enabled=True,
    ) as cluster:
        try:
            logger.info(f"--> Zookeeper ready at {cluster.zookeeper_url} <--")
            logger.info(f"--> Bootstrap Servers {cluster.get_bootstrap_servers('SSL')} <--")
            subprocess.check_call(
                [
                    "/usr/bin/kafkacat",
                    "-L",
                    "-b",
                    ",".join(cluster.get_bootstrap_servers("SSL")),
                    "-X",
                    f"ssl.ca.location={cluster.ssl_server_cert_location}",
                    "-X",
                    "security.protocol=SSL",
                    "-X",
                    f"ssl.keystore.location={cluster.ssl_server_keystore_location}",
                    "-X",
                    f"ssl.keystore.password={cluster.ssl_store_passphrase}",
                ]
            )
            time.sleep(5)
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    main()
