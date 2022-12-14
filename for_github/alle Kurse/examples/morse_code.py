
txt2morse_dict = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.',
            'G':'--.','H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..',
            'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.',
            'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-',
            'Y':'-.--', 'Z':'--..', '1':'.----', '2':'...--', '3':'...--',
            '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..',
            '9':'----.', '0':'-----', ',':'--..--', '.':'.-.-.-', '?':'..--..',
            ';':'-.-.-', ':':'---...', '/':'-..-.', '-':'-....-', '\'':'.----.',
            '(':'-.--.-', ')':'-.--.-', '[':'-.--.-', ']':'-.--.-', '{':'-.--.-',
            '}':'-.--.-', '_':'..--.-'}

morse2txt_dict = dict(zip(txt2morse_dict.values(),
                          txt2morse_dict.keys()))


def txt2morse(txt):
    """ txt2morse wandelt text string in morse ...."""
    result = ""
    for char in txt.upper():
        result += txt2morse_dict[char] + " "
    return result.rstrip()


def morse2txt(morse_txt):
    res = ""
    for morse_word in morse_txt.split("  "):
        for morse_char in morse_word.split():
            res += morse2txt_dict[morse_char]
        res += " "
    return res


if __name__ == "__main__":
    res = txt2morse("aBAC bac")
    orig = morse2txt(res)
    print(orig)
