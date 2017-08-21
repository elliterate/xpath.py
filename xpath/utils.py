from xpath.compat import bytes_


def decode_bytes(value):
    """ str: Decodes the given byte sequence. """
    return value.decode("utf-8") if isinstance(value, bytes_) else value
