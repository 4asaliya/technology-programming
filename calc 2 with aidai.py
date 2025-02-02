membership=(input("Введите членство:"))
amount=float(input("Введите сумму:"))

if membership==("золото"):
  if amount >100 :
   discount=0.2
  else:
    discount=0.1

if membership==("серебро"):
  if amount >100 :
   discount=0.15
  else:
    discount=00.5

if membership==("обычный"):
  if amount >100 :
   discount=00.5
  else:
    discount=0

discount_amount=amount*discount
final_price=amount - discount_amount

print(f"Скидка:{discount *100:.0f}%")
print(f"Итоговая сумма :${final_price:2f}")
