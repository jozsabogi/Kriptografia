import pytest
import solitaire

def test_solitaire_step_a():
    key1 = [53, 54] + my_range(1,52)
    assert solitaire.step_a(key1) == [54, 53] + my_range(1,52)

    key2 = my_range(1,7) + [53] + my_range(8,20) + [54] + my_range(21,52)
    assert solitaire.step_a(key2) == ( my_range(1,7)
        + [8, 53] + my_range(9,20) + [54] + my_range(21,52) )

    key3 = my_range(1,52) + [54, 53]
    assert solitaire.step_a(key3) == [1, 53] + my_range(2, 52) + [54]

    key4 = my_range(1,52) + [53, 54]
    assert solitaire.step_a(key4) == my_range(1, 52) + [54, 53]

def test_solitaire_step_b():
    key1 = [54, 53] + my_range(1,52)
    assert solitaire.step_b(key1) == [53, 1, 54] + my_range(2,52)

    key2 = my_range(1,20) + [54] + my_range(21,53)
    assert solitaire.step_b(key2) == my_range(1,22) + [54] + my_range(23,53)

    key3 = my_range(3,53) + [54, 1, 2]
    assert solitaire.step_b(key3) == my_range(3,53) + [1, 2, 54]

    key4 = my_range(1,52) + [54, 53]
    assert solitaire.step_b(key4) == [1, 54] + my_range(2, 52) + [53]

    key5 = my_range(1,53) + [54]
    assert solitaire.step_b(key5) == [1, 2, 54] + my_range(3, 53)

def test_solitaire_step_c():
    key1 = [1, 2, 53] + my_range(3,20) + [54] + my_range(21,52)
    assert solitaire.step_c(key1) == ( my_range(21,52) 
        + [53] + my_range(3,20) + [54, 1, 2] )

    key2 = [1, 2, 54] + my_range(3,20) + [53] + my_range(21,52)
    assert solitaire.step_c(key2) == ( my_range(21,52)
        + [54] + my_range(3,20) + [53, 1, 2] )

    key3 = [53] + my_range(1,20) + [54] + my_range(21,52)
    assert solitaire.step_c(key3) == ( my_range(21,52)
        + [53] + my_range(1,20) + [54] )

    key4 = [1, 2, 53] + my_range(3,52) + [54]
    assert solitaire.step_c(key4) == [53] + my_range(3,52) + [54, 1, 2] 

    key5 = [53] + my_range(1,52) + [54]
    assert solitaire.step_c(key5) == [53] + my_range(1,52) + [54]

def test_solitaire_step_d():
    key1 = my_range(1,52) + [54, 53]
    assert solitaire.step_d(key1) == my_range(1,52) + [54, 53]

    key2 = my_range(1,24) + my_range(26,54) + [25]
    assert solitaire.step_d(key2) == ( 
        my_range(27,54) + my_range(1,24) + [26, 25] )

def test_solitaire_step_e():
    key1 = [54] + my_range(1,53)
    assert solitaire.step_e(key1) == -1

    key2 = [5, 1, 2, 3, 4] + my_range(6,54)
    assert solitaire.step_e(key2) == 6

def test_solitaire():
    key = [1, 2, 53,3, 4] + my_range(8, 52) + [54, 5, 6, 7]
    # a, b: [1, 2, 3, 53, 4] + my_range(8, 52) + [5, 6, 54, 7]
    # c: [7, 53, 4] + my_range(8, 52) + [5, 6, 54, 1, 2, 3]
    # d: my_range(8, 52) + [5, 6, 54, 1, 2, 7, 53, 4, 3]
    # e: 16
    assert solitaire.solitaire(key) == (
        16, my_range(8, 52) + [5, 6, 54, 1, 2, 7, 53, 4, 3] )

def test_solitaire_encrypt_decrypt():
    key = solitaire.generate_key()
    message = b'solitaire'

    (result, new_key_1) = solitaire.encrypt_solitaire(message, key)

    (decrypted, new_key_2) = solitaire.decrypt_solitaire(result, key)

    assert message == decrypted, new_key_1 == new_key_2

def test_solitaire_combine_keys():
    key1 = [2,3,4,1]
    key2 = [2,1,4,3]

    assert solitaire.combined_keys(key1,key2) == [1,4,3,2]
    assert solitaire.combined_keys(key2,key1) == [3,2,1,4]


def my_range(a, b):
    return list(range(a,b+1))
