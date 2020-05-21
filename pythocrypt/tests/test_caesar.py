from pythocrypt.caesar import encrypt, decrypt, brute_force_decryption

# Tests for encryption


def test_plain_encrypt():
    assert(encrypt("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == "DEFGHIJKLMNOPQRSTUVWXYZABC")


def test_plain_encrypt_lowercase():
    assert (encrypt("abcdefghijklmnopqrstuvwxyz") == "defghijklmnopqrstuvwxyzabc")


def test_full_phrase_encrypt_with_shift():
    assert(encrypt("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG", shift=23) ==
           "QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD")

# Tests for decryption


def test_plain_decrypt():
    assert(decrypt("DEFGHIJKLMNOPQRSTUVWXYZABC") == "ABCDEFGHIJKLMNOPQRSTUVWXYZ")


def test_plain_decrypt_lowercase():
    assert (decrypt("defghijklmnopqrstuvwxyzabc") == "abcdefghijklmnopqrstuvwxyz")


def test_full_phrase_decrypt_with_shift():
    assert(decrypt("QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD", shift=23) ==
           "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG")

# Tests for brute force decryption


def test_brute_force_decryption_results():
    messages_decrypted = brute_force_decryption("DEFGHIJKLMNOPQRSTUVWXYZABC", 1, 23)

    for message in messages_decrypted:
        if message == "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            assert True
            return

    assert False


def test_brute_force_decryption_length():
    messages_decrypted = brute_force_decryption("DEFGHIJKLMNOPQRSTUVWXYZABC", 1, 23)
    assert(len(messages_decrypted) == 22)

