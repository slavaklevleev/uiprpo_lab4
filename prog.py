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