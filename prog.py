import re

f = open("data.txt", "r")
Lines = f.readlines()

def phone_format(n):                                                                                                                                  
    return (format(int(n[:-1]), ",").replace(",", "-") + n[-1]).replace("-", " (", 1).replace("-", ") ", 1)

for line in Lines:
    arr = line.strip().split('|')
    for idx, elem in enumerate(arr):
        newString = []
        if idx == 0:
            name = re.sub(r'(?<=[a-z])([A-Z])', r' \1', elem).strip()
            newString.append(name)
        if idx == 1:
            age = re.search(r'[0-9]+', elem)
            if age:
                newString.append(elem)
            else:
                newString.append('')
        if idx == 2:
            phone = '+' + phone_format(elem.replace(' ', ''))
            newString.append(phone)
        # if idx == 3:
            # print('Email')

    # print(arr)
