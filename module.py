# #problmes1
# import my_module as mod
# mod


# #problems2
# from random import choice
# a = []
# names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
# for i in range(4):
#     a.append(choice(names))
# print(a)

# #problems3
# import sys
# print(sys.platform)


# #problems4
# i = input('Аргументы: ')
# def print_args(a):
#     print(eval(a))
# print_args(i)

# #problems5
# from random import randint
# from os import system
# for i in range(5):
#     r = randint(1, 10)
#     system(f'touch /home/beksultan/Desktop/{r}.txt')
# print('Файлы созданы')

# #problems6
# import random
# names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
# t1 = []
# t2 = []
# t3 = []
# t4 = []
# count = 1
# len_t = len(names)//4
# while names != []:
#     name = random.choice(names)
#     if count <= len_t:
#         t1.append(name)
#         names.remove(name)
#     elif count <= len_t * 2:
#         t2.append(name)
#         names.remove(name)
#     elif count <= len_t * 3:
#         t3.append(name)
#         names.remove(name)
#     else:
#         t4.append(name)
#         names.remove(name)
#     count+=1
# print(t1,t2,t3,t4)

# #problems7
# import sys
# sys.argv = eval(input('Введите аргументы: '))
# sys.argv

# #problems8
# import sys
# a = int(input('Первое число: '))
# b = int(input('Второе число: '))
# print(sys.getsizeof(a))
# print(sys.getsizeof(b))

# #problems9
# from random import choice
# a = int(input('Введите число для генерации пароля: '))
# b = ''
# s = 'qwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*()/|?'
# for i in range(a):
#     b+=choice(s)
# print(b)

# #problems10
# import random
# user = input("Выберите один из них - камень, ножницы или бумага: ")
# possible_actions = ["камень", "бумага", "ножницы"]
# computer = random.choice(possible_actions)
# if user.lower() == computer:
#     print("Ничья, оба выбрали один тот же предмет")
# elif user.lower() == "камень":
#     if computer == "ножницы":
#         print("Камень бьет ножницы! Вы победили!")
#     else:
#         print("Бумага оборачивает камень! Вы проиграли.")
# elif user.lower() == "бумага":
#     if computer == "камень":
#         print("Бумага оборачивает камень! Вы победили!")
#     else:
#         print("Ножницы режут бумагу! Вы проиграли.")
# elif user.lower() == "ножницы":
#     if computer == "бумага":
#         print("Ножницы режут бумагу! Вы победили!")
#     else:
#         print("Камень бьет ножницы! Вы проиграли.")


#problems11
# from random import randrange
# print(randrange(6, 12, 2))
# print(randrange(5, 100, 5))

#problems12

# #ПЕРЕИМНОВАНИЕ ФАЙЛА С ПОМОЩЬЮ  OS
# import os
# os.rename("text.txt", "renamed-text.txt")

#Если тебе еще не больше 18 лет прога выйдет.
# import sys
# age = int(input('Введите возраст: '))
# if age < 18:
#     sys.exit("Требуемый возраст: 18!")    
# else:
#     print("Проходите")

#problems13
# import datetime
# a = datetime.datetime.now()
# b = datetime.timedelta(days=1000)
# result = a+b
# print(result)

##ПОВТОРЕНИЕ
##1
# numbers = [1, 12, 123, 1234, 12345, 123456, 1234567, 12345678, 123456789]
# f = []
# for i in range(1,len(numbers)):
#     f.append(numbers[i]+numbers[i-1])
# print(f)

# #2
# import datetime
# a = datetime.datetime.now()
# print(a)

# #3
# import time
# for i in range(10):
#     time.sleep(1)
#     print()

# #4
# list1 = [1,3,5,7,9,11,13]
# list2 = [2,4,6,8,10,12,14]
# res = zip(list1,list2)
# for i,j in res:
#     print(i,j)






























