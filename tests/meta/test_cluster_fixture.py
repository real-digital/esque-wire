from tests.cluster_fixture import Cluster


def test_simple_startup(kafka_version):
    with Cluster(kafka_version=kafka_version) as cluster:
        cluster.bootstrap_servers("PLAINTEXT")
