#!/bin/env python

import logging
import pathlib
import subprocess
from typing import List

import requests
import sys
import tempfile
import tarfile

log = logging.getLogger(__name__)

PARENT_DIR = pathlib.Path(__file__).resolve().parent

JYTHON_VERSION = "2.7.1"
JYTHON_JAR = f"jython-standalone-{JYTHON_VERSION}.jar"
JYTHON_PATH = PARENT_DIR / JYTHON_JAR

KAFKA_VERSION = "2.3.0"
KAFKA_LIB_PATH = PARENT_DIR / f"kafka_2.11-{KAFKA_VERSION}" / "libs"


def main(argv: List[str]):
    log_level = logging.INFO
    if '--log-level' in argv:
        idx = argv.index('--log-level')
        value = argv[idx+1].upper()
        log_level = getattr(logging, value)

    logging.basicConfig(level=log_level)

    if not JYTHON_PATH.exists():
        log.info("Jython not present.")
        download_jython()
    if not KAFKA_LIB_PATH.exists():
        log.info("Kafka not present.")
        download_kafka()

    log.info("running Jython to generate api_definition.json")
    subprocess.check_call([
        "java",
        "-cp", f"{JYTHON_PATH}:{KAFKA_LIB_PATH}/*",
        "org.python.util.jython",
        str(PARENT_DIR / "_schema_generator.py")
    ])
    log.info("done")


def download_jython():
    url = ("http://search.maven.org/remotecontent?filepath=org/python/jython-standalone"
           f"/{JYTHON_VERSION}/jython-standalone-{JYTHON_VERSION}.jar")
    local_file = JYTHON_PATH
    download_file(url, local_file)


def download_file(url: str, local_file: pathlib.Path):
    log.info(f"Downloading from {url} to {local_file}.")
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with local_file.open("wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:  # filter out keep-alive chunks
                    f.write(chunk)


def download_kafka():
    url = ("https://archive.apache.org/dist/kafka/"
           f"{KAFKA_VERSION}/kafka_2.11-{KAFKA_VERSION}.tgz")

    def is_lib(member: tarfile.TarInfo) -> bool:
        return member.name.startswith(f"kafka_2.11-{KAFKA_VERSION}/libs/")

    with tempfile.NamedTemporaryFile(suffix='.tgz') as tmpfile:
        download_file(url, pathlib.Path(tmpfile.name))
        tmpfile.file.seek(0)
        log.info("extracting jars")
        with tarfile.open(tmpfile.name) as tar:
            members = [mem for mem in tar.getmembers() if is_lib(mem)]
            tar.extractall(members=members, path=PARENT_DIR)


if __name__ == "__main__":
    main(sys.argv)
