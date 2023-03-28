morse_dict = {
    'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---',
    'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'-.-', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----', ',':'--..--',
    ':':'---...', "'":'.----.', '.':'.-.-.-', '?':'..--..'
}


def make_morse(sentence):
    morse_list = []
    for character in sentence:
        if character.upper() in morse_dict:
            morse_list.append(morse_dict[character.upper()])
    return morse_list


print(make_morse('and i hate It when it happens.'))
