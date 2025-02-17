words = (input("Введите слово:"))
letters1 = 'aeiou'
vowels = 0
consonats = 0

for word in words:
    if word in letters1:
        vowels +=1
    else:
        consonats +=1
print(f"Гласных букв:{vowels}")
print(f"Согласных букв:{consonats}")
