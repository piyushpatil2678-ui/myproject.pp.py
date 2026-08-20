text = input("Enter a text: ")
key = int(input("Enter a key: "))
n = int(input("Rounds: "))

def columnar(text, key):
    # spaces remove
    text = text.replace(" ", "")

    # padding
    while len(text) % key != 0:
        text += "*"

    result = ""

    # column-wise reading
    for i in range(key):
        for j in range(i, len(text), key):
            result += text[j]

    return result


result = text

for r in range(n):
    result = columnar(result, key)
    print("Round", r + 1, ":", result)

print("Final Result:", result)
