from pythocrypt.rail_fence import encrypt, decrypt, brute_force


def test_rail_fence_encrypt():
    assert(encrypt("Buy more Maine potatoes") == "BYOEANPTTEUMRMIEOAOS")


def test_rail_fence_encrypt_with_3_fences():
    assert (encrypt("WAFFLES FOR BREAKFAST", rails=3) == "WLOEAAFEFRRAFSFSBKT")


def test_rail_fence_encrypt_with_4_fences():
    assert (encrypt("WAFFLES FOR BREAKFAST", rails=4) == "WSETAEFRASFLOBKAFRF")


def test_rail_fence_encrypt_with_100_fences():
    assert (encrypt("WAFFLES FOR BREAKFAST", rails=100) == "WAFFLESFORBREAKFAST")


def test_rail_fence_decrypt():
    assert(decrypt("BYOEANPTTEUMRMIEOAOS", 2) == "BUYMOREMAINEPOTATOES")


def test_rail_fence_decrypt_with_3_fences():
    assert (decrypt("WLOEAAFEFRRAFSFSBKT", 3) == "WAFFLESFORBREAKFAST")


def test_rail_fence_decrypt_with_4_fences():
    assert (decrypt("WSETAEFRASFLOBKAFRF", 4) == "WAFFLESFORBREAKFAST")


def test_rail_fence_decrypt_with_6_fences():
    assert (decrypt("WBARRFOETFFASLSKAEF", 6) == "WAFFLESFORBREAKFAST")


def test_brute_force():
    words = brute_force("WSETAEFRASFLOBKAFRF")
    for word in words:
        if word == "WAFFLESFORBREAKFAST":
            assert True
            return

    assert False
