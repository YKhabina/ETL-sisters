N = int(input("Введите количество чисел N: "))

numbers = []

for i in range(N):
    num = int(input(f"Введите {i+1}-е целое число: "))
    numbers.append(num)

print(f"\nИсходный массив: {numbers}")

sorted_numbers = sorted(numbers)

print(f"Отсортированный массив: {sorted_numbers}")

minimum = min(sorted_numbers)  
maximum = max(sorted_numbers)  

print(f"Минимальное число: {minimum}")
print(f"Максимальное число: {maximum}")