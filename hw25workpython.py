
# d1 = {'animal': 'cat1', 'animal': 'cat2'}   #dict
# d2 = ('cat1', 'cat2')                       #tuple
# mas = ['cat1', 'cat2']                      #list
# new = input('цого добавить\n')
# mas.append(new)                             #добавить в массив 1 слово
# print(mas)
# mas.extend(d2)                              #добавить несколько слов или массив
# print(mas)
# mas.pop()                                   #удаление одного элемента(последнего или по индексу)
# print(mas)
# mas.remove('cat')                           #удаляет из массива по значению
# print(mas)
#
# i = print(mas.index('cat'))
#
# try:
#     mas.remove('cat')                      #метод для обхода ошибки
#     print(mas)
# except:
#     print('no no')

# mas = ['nissan', 'audi', 'uaz']
# def new():
#     new = input('цого добавить\n')
#     mas.append(new)
#     print(mas)
# def dell():
#     dell = input('что удалить\n')
#     try:
#         mas.remove(dell)
#         print(mas)
#     except:
#         print('такой нет')
#
#
#
# a = input('нажми 1 чтобы добавить или 2 чтобы удалить')
# if a == '1':
#     new()
# elif a == '2':
#     dell()
# else:
#     print('ошибка')

# mas = ['cat', 'dog', 'frog', 'cat']
# a = mas.index('cat',1)                         #находит номер элементы в массиве
# print('под номером',a)
#
# b = mas.count('cat')                           # считает количество одинаковых элементов, не выдает ошибку если элемента нет
# print('под номером',a)
#
# def f1():
#     n = input('кого удалить\n')
#     if mas.count(n)>0:
#         mas.remove(n)
#     print(mas)
#     pass
# f1()

# num = [2, 3, 4, 5, 9, 7, 1, 6]
# bukv = ['asd', 'abc', 'qwe', 'q']
# num.sort()                                      #сортировка
# print(num)
# bukv.sort()
# print(bukv)
# num.reverse()                                   # разворот массива
# print(num)

# import random
# a = []
# for i in range(20):
#     a.append(random.randint(1,100))
# print(a)
# print(max(a))
# print(min(a))
#Задача 1.
# mas = ['Ivanov', 'Petrov', 'Sidorov']
# print(mas)
#
# while True:
#     a = input('Студенты: 1-добавить, 2-удалить, 3-найти, 4-выход\n')
#
#     if a == '1':
#         b = input('Напишите фамилию, которую нужно добавить: ')
#         mas.append(b)
#         print(mas)
#     elif a == '2':
#         b = input('Напишите фамилию, которую нужно удалить: ')
#         mas.remove(b)
#         print(mas)
#     elif a == '3':
#         b = input('Напишите фамилию, которую нужно найти: ')
#         if b in mas:
#             c = mas.index(b)
#             print('Номер студента:', c)
#         else:
#             print('Студент не найден')
#     elif a == '4':
#         print('Выход из программы.')
#         break
#     else:
#         print('Некорректный ввод. Повторите попытку.')
#Задача2
# import random
# mas = ['Ivanov', 'Petrov', 'Sidorov', 'Kozlov', 'Van', 'Pukan', 'Str','Hehey', 'Grob', 'Sidr']
# print(mas)
#
# a = []
# for x in range(len(mas)):
#     grade = random.randint(2, 5)
#     a.append(grade)
#
# for i in range(len(mas)):
#     print(f"{mas[i]} - {a[i]}")
#Задача3.
import random

# Создание списка из 30 случайных чисел
numbers = []
for x in range(30):
    number=random.randint(10,50)
    numbers.append(number)
print("Исходный список:", numbers)

# Находим первый максимум
first_max = max(numbers)
numbers.remove(first_max)

# Находим второй максимум
second_max = max(numbers)
numbers.remove(second_max)

# Находим третий максимум
third_max = max(numbers)

print("Первый максимум:", first_max)
print("Второй максимум:", second_max)
print("Третий максимум:", third_max)