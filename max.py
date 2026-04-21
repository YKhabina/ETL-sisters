num1 = int(input("Введите первое целое число: "))
num2 = int(input("Введите второе целое число: "))

if num1 > num2:
    maximum = num1
else:
    maximum = num2

print(f"Максимальное из чисел {num1} и {num2} равно: {maximum}")
