array = []
symbols = set()
while True:
    word = input()
    if (word.__getitem__(0) == ' '):
        print("first symbol should not be a space!")
    else:
        if (not word.__contains__(" ")):
            print("You should enter 1 space!")
        else:
            break

for i in range(len(word)):
    if (not word.__getitem__(i).__eq__(" ")):
        array.append(word.__getitem__(i))
    else:
        break
for i in range(len(array)):
    if (ord(array[i]) < 48):
        continue
    elif (ord(array[i]) >= 48 and ord(array[i]) <= 57):
        symbols.add(array[i])
    elif (ord(array[i]) >= 58 and ord(array[i]) <= 64):
        continue
    elif (ord(array[i]) >= 65 and ord(array[i]) <= 90):
        array[i] = chr(ord(array[i]) + 32)
        symbols.add(array[i])
    elif (ord(array[i]) >= 91 and ord(array[i]) <= 96):
        continue
    elif (ord(array[i]) >= 97 and ord(array[i]) <= 122):
        symbols.add(array[i])
print(symbols)
