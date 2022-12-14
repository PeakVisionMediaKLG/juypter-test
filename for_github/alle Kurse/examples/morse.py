char_morse={'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.',
            'G':'--.','H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..',
            'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.',
            'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-',
            'Y':'-.--', 'Z':'--..', '1':'.----', '2':'...--', '3':'...--',
            '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..',
            '9':'----.', '0':'-----', ',':'--..--', '.':'.-.-.-', '?':'..--..',
            ';':'-.-.-', ':':'---...', '/':'-..-.', '-':'-....-', '\'':'.----.',
            '(':'-.--.-', ')':'-.--.-', '[':'-.--.-', ']':'-.--.-', '{':'-.--.-',
            '}':'-.--.-', '_':'..--.-'}

def txt2morse(txt):
    morse_code = ""
    # berechnung
    for char in txt.upper():
        if char == " ":
            morse_code += "   "
        else:
            morse_code += char_morse[char] + " "
    return morse_code

print(txt2morse("Hi"))
print(txt2morse("So what?"))
