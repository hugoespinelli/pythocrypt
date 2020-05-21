"""
Module for rail fence cipher.
In the rail fence cipher, the plain text is written downwards and diagonally on successive
"rails" of an imaginary fence, then moving up when the bottom rail is reached. When the top rail
is reached, the message is written downwards again until the whole plaintext is written out.
The message is then read off in rows.
"""


def encrypt(message: str, rails: int = 2) -> str:
    """
    Function to encrypt with rail fence cipher

    :param message: message to be encrypted
    :param rails: number of rails to be used
    :return: encrypted message
    """
    message_encrypted = message.replace(" ", "").upper()

    slices = _slice_rails(message_encrypted, rails)

    message_encrypted = "".join(slices)
    return message_encrypted


def _slice_rails(message, rails):
    slices = [[] for i in range(rails)]

    slice_index = 0
    step = 1

    for letter in message:
        slices[slice_index].append(letter)

        if slice_index >= (rails-1) or (slice_index + step) <= -1:
            step = step * (-1)

        slice_index = slice_index + step

    slices = [''.join(s) for s in slices]
    return slices


def decrypt(message: str, rail: int) -> str:

    rails = [[] for _ in range(rail)]

    slice_index = 0
    letter_counter = 0

    cycle_units = _cycle_units(rail)
    full_cycles = len(message) // cycle_units

    remaining_letters = len(message) % cycle_units

    j = 0
    while j < len(message):

        rails[slice_index].append(message[j])
        letter_counter += 1

        if _is_end_of_edge_rail(slice_index,
                                letter_counter,
                                full_cycles) or _is_end_of_middle_row(letter_counter, full_cycles):

            if remaining_letters > 0:
                remaining_letters -= 1
                j += 1
                rails[slice_index].append(message[j])

            letter_counter = 0
            slice_index += 1

        j += 1

    message_decrypted = _rails_decryption(rails, len(message))
    print(message_decrypted)

    return message_decrypted


def _rails_decryption(rails, message_len):

    slice_index = 0
    step = 1

    message = ""

    for _ in range(message_len):

        message += rails[slice_index].pop(0)

        if slice_index >= (len(rails) - 1) or (slice_index + step) <= -1:
            step = step * (-1)

        slice_index = slice_index + step

    return message


def _is_end_of_edge_rail(slice_index, counter, cycles):
    return slice_index == 0 and counter == cycles


def _is_end_of_middle_row(counter, cycles):
    return counter == cycles * 2


def _number_of_letters_in_rails(cycles, cycle_size):
    return cycles * cycle_size


def _cycle_units(rails):
    return (rails * 2) - 2
