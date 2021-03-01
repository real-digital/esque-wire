import pathlib

from OpenSSL import crypto

TEN_YEARS_IN_SECONDS = 315360000


def cert_gen() -> crypto.PKCS12:
    # create a key pair
    k = crypto.PKey()
    k.generate_key(crypto.TYPE_RSA, 4096)
    # create a self-signed cert
    cert = crypto.X509()
    subject = cert.get_subject()
    subject.C = "CC"
    subject.ST = "stateOrProvinceName"
    subject.L = "localityName"
    subject.O = "organizationName"  # noqa
    subject.OU = "organizationUnitName"
    subject.CN = "localhost"
    subject.emailAddress = "emailAddress@example.com"
    cert.set_serial_number(0)
    cert.gmtime_adj_notBefore(0)
    cert.gmtime_adj_notAfter(TEN_YEARS_IN_SECONDS)
    cert.set_issuer(cert.get_subject())
    cert.set_pubkey(k)
    cert.sign(k, "sha512")

    keystore = crypto.PKCS12()
    keystore.set_certificate(cert)
    keystore.set_privatekey(k)

    return keystore


def dump_cert_data(key_file: pathlib.Path, cert_file: pathlib.Path, keystore: crypto.PKCS12) -> None:
    with cert_file.open("wt") as f:
        f.write(crypto.dump_certificate(crypto.FILETYPE_PEM, keystore.get_certificate()).decode("utf-8"))
    with key_file.open("wt") as f:
        f.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, keystore.get_privatekey()).decode("utf-8"))


def dump_keystore(pkcs12_file: pathlib.Path, keystore: crypto.PKCS12, passphrase: str) -> None:
    with pkcs12_file.open("wb") as f:
        f.write(keystore.export(passphrase=passphrase))
