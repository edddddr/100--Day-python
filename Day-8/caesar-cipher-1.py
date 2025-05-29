
direction = input("Type 'encode' to encrypt type 'decode' to decrypt : \n")
text = input("Type your message: \n").lower()
shift = int(input("Type shift number: \n"))

alphabet =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(cipher_direction, plain_text, shift_amount):
    if shift_amount > len(alphabet):
        shift_amount = shift_amount % len(alphabet)


    end_text = ""
    for letter in plain_text:
        possition = alphabet.index(letter)
        if cipher_direction == "encode":
            new_posstion = possition + shift_amount
        else:
             new_posstion = possition - shift_amount
        new_letter = alphabet[new_posstion]
        end_text += new_letter
    print(f"Here's the {cipher_direction} result: {end_text}")

    agin = input("Type 'yes' if you want to go again. Otherwiae type 'no' ")
    if agin != 'no':
        repeat()

def repeat():
    direction = input("Type 'encode' to encrypt type 'decode' to decrypt : \n")
    text = input("Type your message: \n").lower()
    shift = int(input("Type shift number: \n"))

    caesar(direction, text, shift)

caesar(direction = direction, text = text, shift = shift)