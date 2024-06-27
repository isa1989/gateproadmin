import hashlib


def calculate_signature(time, public_key, private_key):
    data = time + public_key + private_key
    encoded_data = data.encode("utf-8")

    # Calculate SHA-256 hash of the encoded data
    sha256_hash = hashlib.sha256(encoded_data)
    return sha256_hash.hexdigest()
