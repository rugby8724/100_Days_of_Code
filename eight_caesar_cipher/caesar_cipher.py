from art import logo as logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
    if shift > 26:
        shift %= 26
    new_text = ''
    for l in text:
        if l not in alphabet:
            new_text += l
            continue
        n = alphabet.index(l)
        if direction == 'encode':
            if n + shift <= 25:
                new_text += alphabet[n+shift]
            else:
                new_text += alphabet[n+shift-26]
        elif direction == 'decode':
            new_text += alphabet[n-shift]
    print(f'The {direction}d text is {new_text}')

print(logo)

code = True

while code == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)

    another_code = input('Would you like to encode or decode another message y or n ?  ').lower()
    if another_code == 'n':
        code = False
    else:
        continue
