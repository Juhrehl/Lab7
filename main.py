LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS = LETTERS.lower()

def encryption(message, shift):
    encrypted = ""
    for characters in message:
        if characters in LETTERS:
            number = LETTERS.find(characters)
            number += shift
            encrypted += LETTERS[number]

    return encrypted

def decryption(message, shift):
    decrypted = ""
    for characters in message:
        if characters in LETTERS:
            number = LETTERS.find(characters)
            number -= shift
            decrypted +=  LETTERS[number]

    return decrypted

def main():
    message = str(input("Enter a sentence: "))
    shift = int(input("Enter your shift number: "))
    choice = input("Do you want to encrypt or decrypt? [E/D]: ")

    if choice.lower():
        print(encryption(message, shift))
    else:
        print(decryption(message, shift))

main()