f = open("data.txt", "r")
Lines = f.readlines()

for line in Lines:
    arr = line.strip().split('|')
    print(arr)