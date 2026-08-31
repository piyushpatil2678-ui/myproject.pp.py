def rail_fence_encrypt(text, rails):
    fence = [[] for _ in range(rails)]

    row = 0
    direction = 1

    for char in text:
        fence[row].append(char)

        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1

        row += direction

    result = ""

    for rail in fence:
        result += "".join(rail)

    return result


text = input("Enter text: ")
rails = int(input("Enter number of rails: "))
