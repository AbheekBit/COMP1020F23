import random

with open("1000sentence.txt") as file:
    lines = file.readlines()

while True:
    #print(lines[random.randrange(0, len(lines))])
    user_input = input()
    words = user_input.split(" ")
    keyword = words[-1]

    if keyword == "Stop":
        break

    hasPrinted = False
    for sentence in lines:
        if keyword in sentence:
            print(sentence)
            hasPrinted = True
            break
    if not hasPrinted:
        print(lines[random.randrange(0, len(lines))])