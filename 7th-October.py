# Добавление элемента в конец списка
# myList = [1, 2, 3, 4, 5]
# myList.append(6)
# print(myList)
from itertools import count

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

# Матрица
count = 1
matrix = []
for i in range(3):
    matrix.append(list(range(1, 4)))

print(matrix)