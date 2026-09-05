import random

key = {
    'A': ['11', '21', '31'],
    'B': ['12', '22'],
    'C': ['13', '23'],
    'D': ['14', '24'],
    'E': ['15', '25', '35', '45'],
    'F': ['16', '26'],
    'G': ['17', '27'],
    'H': ['18', '28'],
    'I': ['19', '29'],
    'J': ['20', '30'],
    'K': ['32', '42'],
    'L': ['33', '43'],
    'M': ['34', '44'],
    'N': ['36', '46'],
    'O': ['37', '47'],
    'P': ['38', '48'],
    'Q': ['39', '49'],
    'R': ['40', '50'],
    'S': ['41', '51'],
    'T': ['52', '62'],
    'U': ['53', '63'],
    'V': ['54', '64'],
    'W': ['55', '65'],
    'X': ['56', '66'],
    'Y': ['57', '67'],
    'Z': ['58', '68']
}


def encrypt(text):
    result = ""

    for char in text.upper():
        if char in key:
            result += random.choice(key[char]) + " "
        elif char == " ":
            result += "/ "

    return result.strip()


def decrypt(ciphertext):
    reverse_key = {}

    for letter, codes in key.items():
        for code in codes:
            reverse_key[code] = letter

    result = ""

    for code in ciphertext.split():
        if code == "/":
            result += " "
        elif code in reverse_key:
            result += reverse_key[code]

    return result


form = input("Enter (E) for encryption or (D) for decryption: ").upper()

if form == 'E':

    text = input("Enter plaintext: ")

    encrypted_text = encrypt(text)

    print("Encrypted text:", encrypted_text)


elif form == 'D':

    text = input("Enter ciphertext: ")

    decrypted_text = decrypt(text)

    print("Decrypted text:", decrypted_text)


else:
    print("Invalid choice!")
