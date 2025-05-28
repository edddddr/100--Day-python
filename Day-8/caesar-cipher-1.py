
direction = input("Type 'encode' to encrypt type 'decode' to decrypt : \n")
text = input("Type your message: \n").lower()
shift = int(input("Type shift number: \n"))

alphabet =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(plain_text, shift_amount):
    cipher = ""
    for letter in plain_text:
        possition = alphabet.index(letter)
        new_posstion = possition + shift_amount
        new_letter = alphabet[new_posstion]
        cipher += new_letter
    print(cipher)

encrypt(text, shift)