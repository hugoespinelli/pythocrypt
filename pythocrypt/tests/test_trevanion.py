
from pythocrypt.trevanion import encrypt, decrypt


def test_cipher_encryption():
    message_encrypted = encrypt("code me", 3)
    assert decrypt(message_encrypted, 3) == "codeme"


def test_cipher_decryption():
    assert decrypt("""Worthie Sir John: Hope, that is the beste comfort of the afflicted,
cannot much, I fear me, help you now. That I would saye to you,
is this only: if ever I may be able to requite that I do owe you,
stand not upon asking me. 'Tis not much I can do: but what I
can do, bee you verie sure I wille. I knowe that, if deathe comes,
if ordinary men fear it, it frights not you, accounting for it for a
high honour, to have such a rewarde of your loyalty. Pray yet that
you may be spared this soe bitter, cup. I fear not that you will
grudge any sufferings; onlie if bie submission you can turn them
away, 'tis the part of a wise man. Tell me, an if you can, to do for
you anythinge that you wolde have done. The general goes back
on Wednesday. Restinge your servant to command. R.T.""", 3) == "panelateastendofchapelslides"
