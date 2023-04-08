import hashlib


def get_hash(message: str):
    m = hashlib.sha512()
    m.update(message.encode("UTF-8"))
    return m.hexdigest()


def check_hash(message: str, hash_val: str):
    return get_hash(message) == hash_val

    
