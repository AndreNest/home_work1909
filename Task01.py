# 1 - Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]

num = int(input("Введите число: "))
list_num = []
i = 2 
start_num = num
while i <= num:
    if num % i == 0:
        list_num.append(i)
        num //= i
        i = 2
    else:
        i += 1

print(f"Множители числа {start_num} ----->: {list_num}")