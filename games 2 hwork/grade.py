grade=int(input("Введите оценку за тест (0-100):"))
if grade>=90:
    homework_done=input("Сдали ли вы все задания (да/нет):")
    if homework_done=="да":
        print("отлично!оценка А+")
    else:
        print("Хорошая работа,но сдайте все работы!оценка А")
elif 80<=grade<90:
    attendance=input("Посещали ли вы более 75% занятий (да/нет)")
    if attendance=="да":
        print("хорошо!оценка B")
    else:
        print("Нужно посещать занятия! Оценка С")
else:
    print("Старайтесь лучше!")

