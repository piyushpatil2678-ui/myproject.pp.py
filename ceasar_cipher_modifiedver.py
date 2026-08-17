# Caesar Cipher (Encryption + Decryption)

text = input("Enter the text: ")
shift = int(input("Enter shift value: "))

choice = input("Encrypt (E) or Decrypt (D): ").upper()

output = ""

for ch in text:
    if 'a' <= ch <= 'z':
        if choice == "E":
            new_char = chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
        else:
            new_char = chr((ord(ch) - ord('a') - shift) % 26 + ord('a'))
        output += new_char

    elif 'A' <= ch <= 'Z':
        if choice == "E":
            new_char = chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
        else:
            new_char = chr((ord(ch) - ord('A') - shift) % 26 + ord('A'))
        output += new_char

    else:
        output += ch

print("Result:", output)