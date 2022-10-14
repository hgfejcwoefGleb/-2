print("Добро пожаловать в первое домашнее задание")
name = input("Введите имя: ")
surname = str(input("Введите фамилию: "))
age = float(input("Введите возраст: "))
print(name + "_" + surname + "_" + str(age))
name, surname = surname, name
age = age+60
print(name + "_" + surname + "_" + str(age))