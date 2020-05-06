def make_key(key: str, key_prefix: str, version: int) -> bytes:
    return f'{key_prefix}{key}'.encode()
