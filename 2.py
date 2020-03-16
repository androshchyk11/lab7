id = 1
students = {}
while True:
    array = []
    surname = input("Прізвище:")
    array.append(surname)
    group = input("Група: ")
    array.append(group)
    while True:
        try:
            ph = int(input("Бал з фізики: "))
            break
        except ValueError as e:
            print("Wrong data!")
    array.append(ph)
    while True:
        try:
            ap = int(input("АП: "))
            break
        except ValueError as e:
            print("Wrong data!")
    array.append(ap)
    while True:
        try:
            vishka = int(input("Вишка: "))
            break
        except ValueError as e:
            print("Wrong data!")
    array.append(vishka)
    students[id] = [array[0], array[1], array[2], array[3], array[4]]
    id += 1
    flag1 = input("More? 1 if yes, any key if no if no: ")
    if flag1 == "1":
        del array
        continue
    elif flag1 == "2":
        break

print("Студенти у яких середній бал вище 75:")
print("\n")
for i in students:
    if (students.get(i).__getitem__(2) + students.get(i).__getitem__(3) + students.get(i).__getitem__(4)) / 3 > 75:
        print(f"Прізвище: {students.get(i).__getitem__(0)};\n"
              f"Група: {students.get(i).__getitem__(1)};\n"
              f"Фізика: {students.get(i).__getitem__(2)};\n"
              f"АП: {students.get(i).__getitem__(3)};\n"
              f"Вишка: {students.get(i).__getitem__(4)}.")
