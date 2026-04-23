# put your python code here
input_str = input("Введите последовательность символов")
if len(input_str) == len(set(input_str)):
    print(f"Строка {input_str} имеет уникальные символы")
else: 
    print(f"К сожалению, в строке {input_str}  повторяются символы")