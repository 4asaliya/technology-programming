number=int(input("Введите число:"))
if number % 2 == 0:
    number_devide=input("число делится на 4? (да/нет):")
    if number_devide=="да":
        print("Число делится на 4")
    else:
        print("обычное четное число")

elif number % 2 != 0:
    devide=input("Делится ли на 5? (да/нет):")
    if devide=="да":
        print("число делится на 5")
    else:
        print("простое нечетное число")


