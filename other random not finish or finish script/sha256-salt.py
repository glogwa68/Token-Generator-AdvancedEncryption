import base64
import hashlib

def check_password(tagged_digest_salt, password):
    """
    Checks the OpenLDAP tagged digest against the given password
    """
    # the entire payload is base64-encoded
    assert tagged_digest_salt.startswith('{SSHA}')

    # strip off the hash label
    digest_salt_b64 = tagged_digest_salt[6:]

    # the password+salt buffer is also base64-encoded.  decode and split the
    # digest and salt
    digest_salt = base64.b64decode(digest_salt_b64)
    digest = digest_salt[:20]
    salt = digest_salt[20:]

    sha = hashlib.sha1(password.encode('utf-8'))
    sha.update(salt)

    return digest == sha.digest()

sha = "{SSHA}SEzETXlz6g2NOCw97cvSnKIomtsEn3TOH8v/BU7e4f+zwa7lAJR4YQ=="
print(check_password(sha, "bullshit"))