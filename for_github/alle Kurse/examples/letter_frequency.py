def letter_frequency(s):
    frequency_dict = {}
    for char in s.lower():
        if char.isalpha():
            if char in frequency_dict:
                frequency_dict[char] += 1
            else:
                frequency_dict[char] = 1
    #f =  frequency_dict.items()      # Python2
    f =  list(frequency_dict.items()) # Python3
    f.sort(key = lambda x: x[1], reverse=True)
    return f

freq = letter_frequency(open("ulysses.txt").read())
print(freq)
