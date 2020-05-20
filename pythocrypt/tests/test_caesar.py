from pythocrypt.caesar import encrypt


def test_plain_encrypt():
    assert(encrypt("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == "DEFGHIJKLMNOPQRSTUVWXYZABC")


def test_plain_encrypt_lowercase():
    assert (encrypt("abcdefghijklmnopqrstuvwxyz") == "defghijklmnopqrstuvwxyzabc")


def test_full_phrase_encrypt_with_shift():
    assert(encrypt("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG", shift=23) ==
           "QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD")

