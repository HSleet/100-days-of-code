import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift):
    cipher_text = []
    for letter in text:
        if letter not in alphabet:
            cipher_text.append(letter)
            continue
        alphabet_position = (alphabet.index(letter) + shift) % 26
        cipher_text.append(alphabet[alphabet_position])
    print(f"Here's the {direction}d result:\n\n{''.join(cipher_text)}")

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction == "encode":
        sign = "+"
    elif direction == "decode":
        sign = "-"
    else:
        print("Invalid input")
        continue
        
    text = input("Type your message:\n").lower()

    shift = input("Type the shift number:\n")
    if not shift.isnumeric():
        print("Please enter only integer numbers")
        continue
        
    shift = int(sign + shift)

    caesar(text, shift)
    if input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower() == "no":
        break
