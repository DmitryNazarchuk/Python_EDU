#Скопировать в файл F2 только четные строки из F1. Подсчитать размер файлов F1 и F2 (в байтах).

import io

# главная программа:
# создание итерируемого объекта - строк файла
main_iter = io.open('hometask4_1.txt')

x = 0
f = open('hometask4_2.txt', 'w')  # clear file
# проход по итерируемому объекту с помощью цикла
for line in main_iter:
    cells = line #
    x += 1  # вывод номера строки
    if x%2 == 0:
        #print("строка" , x, "   " ,cells )
        f = open('hometask4_2.txt', 'a')
        f.write(cells)
        f.close()

import os
with open("hometask4_1.txt") as file:
    file.seek(0, os.SEEK_END)
    #print(file.tell())
    print("размер файла hometask4_1.txt" , file.tell() , "в байтах ")

with open("hometask4_2.txt") as file:
    file.seek(0, os.SEEK_END)
    #print(file.tell())
    print("размер файла hometask4_2.txt" , file.tell() , "в байтах ")
