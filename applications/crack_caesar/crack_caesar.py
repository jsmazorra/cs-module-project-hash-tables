# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
freq_list = [
    "E",
    "T",
    "A",
    "O",
    "H",
    "N",
    "R",
    "I",
    "S",
    "D",
    "L",
    "W",
    "U",
    "G",
    "F",
    "B",
    "M",
    "Y",
    "C",
    "P",
    "K",
    "V",
    "Q",
    "J",
    "X",
    "Z",
]

# Read the file.
with open("ciphertext.txt") as file:
    ciphertext = file.read()

charcount = {}

for char in ciphertext:
    if char in map(chr, range(65, 91)):
        if char not in charcount:
            charcount[char] = 1
        else:
            charcount[char] += 1

cipher_freq = [
    item[0] for item in sorted(charcount.items(), key=lambda x: x[1], reverse=True)
]


lookup = {cipher: plain for cipher, plain in zip(cipher_freq, freq_list)}

# Output in plain text.
print(ciphertext.translate(str.maketrans(lookup)))
