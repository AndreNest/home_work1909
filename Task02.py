# 2 - Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности. Не использовать множества. 
# [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]

list_num = list(map(int, input("Введите числа через пробел: \n").split()))
print(f"Начальный список ---> {list_num}")
new_list_num = []
[new_list_num.append(i) for i in list_num if i not in new_list_num]
print(f"Новый список ---> {new_list_num}")