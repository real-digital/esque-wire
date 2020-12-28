import logging
import sys
import time

from tests.cluster_fixture import Cluster, KafkaVersion, PlaintextEndpoint, SaslEndpoint, SaslMechanism

logger = logging.getLogger(__name__)


def main() -> None:
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    sasl_mechanisms = [SaslMechanism("PLAIN"), SaslMechanism("SCRAM-SHA-512")]
    endpoints = [PlaintextEndpoint(), SaslEndpoint(), SaslEndpoint(name="ASDF")]
    kafka_version = KafkaVersion("1.1.1")
    with Cluster(
        cluster_size=1, endpoints=endpoints, sasl_mechanisms=sasl_mechanisms, kafka_version=kafka_version
    ) as cluster:
        try:
            logger.info(f"--> Zookeeper ready at {cluster.zookeeper_url} <--")
            logger.info(f"--> Bootstrap Servers {cluster.boostrap_servers('SASL_PLAINTEXT')} <--")
            logger.info(f"--> Bootstrap Servers {cluster.boostrap_servers('PLAINTEXT')} <--")
            logger.info(f"--> Bootstrap Servers {cluster.boostrap_servers('ASDF')} <--")
            time.sleep(10)
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    main()
