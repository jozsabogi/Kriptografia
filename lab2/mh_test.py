import pytest
import mh
import utils

def test_mh_private_key_coprimes():
    private_key = mh.generate_private_key()
    assert utils.coprime(private_key[1], private_key[2])
    assert private_key[1] > private_key[2]

def test_mh_private_key_length():
    private_key = mh.generate_private_key()
    assert len(private_key[0]) == 8

    private_key = mh.generate_private_key(5)
    assert len(private_key[0]) == 5

def test_mh_encrypt_decrypt():
    private_key = mh.generate_private_key()
    public_key = mh.create_public_key(private_key)

    p = b'abc';
    c = mh.encrypt_mh(p, public_key)
    d = mh.decrypt_mh(c, private_key)
    assert p == d

    p2 = bytes(range(256))
    c2 = mh.encrypt_mh(p2, public_key)
    d2 = mh.decrypt_mh(c2, private_key)
    assert p2 == d2

