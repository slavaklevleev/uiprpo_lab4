import re

f = open("data.txt", "r")
Lines = f.readlines()

for line in Lines:
    arr = line.strip().split('|')
    for idx, elem in enumerate(arr):
        newString = []
        if idx == 0:
            name = re.sub(r'(?<=[a-z])([A-Z])', r' \1', elem).strip()
            newString.append(name)
        if idx == 1:
            age = re.search(r'[0-9]+', elem)
            print(elem, name.string)
            if age:
                newString.append(age)
            else:
                newString.append('')

        # if idx == 2:
            # print('Телефон')
        # if idx == 3:
            # print('Email')

    # print(arr)
