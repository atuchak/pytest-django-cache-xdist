def make_key(key: str, key_prefix: str, version: int) -> bytes:
    return '{key_prefix}{key}'.format(key_prefix=key_prefix, key=key).encode()
