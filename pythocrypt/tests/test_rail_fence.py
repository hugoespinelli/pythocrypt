from pythocrypt.rail_fence import encrypt, decrypt


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
