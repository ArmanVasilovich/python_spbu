# Добавление элемента в конец списка
# myList = [1, 2, 3, 4, 5]
# myList.append(6)
# print(myList)
from random import random

# Добавление массива цифр от 1 до 100
# nums = []
# for i in range(1, 101):
#     nums.append(i)

# word = input('Введите слово: ')
# wordList = list(word)
# print(wordList)

# # Сортировка + Reverse
# nums2 = [2, 13, 44, 9, 88, 9]
# nums2.sort(reverse=True)
# sortNumns = sorted(nums2)

# Подсчет одинаковых элементов в списке
# print(sortNumns.count(9))

# # Удаляет по значению без возвращения самого значения
# sortNumns.remove(9)
# # Удаление по индексу с возвращением значения
# deletedNum = sortNumns.pop(1)
# print(sortNumns, deletedNum)

# del Array - удаление по индексу без возвращения значения

# # Объедигение списка
# FirstList = [1, 2, 3, 4, 5]
# SecondList = [6, 7, 8, 9, 10]
# FirstList.extend(SecondList)
# SecondList.append('Python')
# print(FirstList)
# print(SecondList)
# #
# ThirdList = [11, 12, 13, 14, 15]
# print(FirstList + ThirdList)

# newList = list(range(1, 21))
# print(newList)

# # Двумерный массив
# FourthList = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(FourthList[0], FourthList[0][1])

# # Матрица
# count = 1
# matrix = []
# for i in range(7):
#     matrix.append(list(range(count, count + 3)))
#     count += 3
#
# # Вывод матрицы
# for i in matrix:
#     for j in i:
#         print(j, end=' ')
#     print()

# List Comprehension
# squares = []
# for i in range(1, 11):
#     squares.append(i**2)
# print(squares)

# List Comprehension (В одну строчку)
# squares = [i**10 for i in range(1, 11)]
# print(squares)

# # List Comprehension (В одну строчку с условием)
# squares = [i**2 if i%2 != 0 else i for i in range(1, 11)]
# print(squares)
