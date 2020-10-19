#"""Для каждого четного по номеру элемента списка A найти его сумму со следующим элементом и записать эти суммы в новый список B."""
import random
n = int(input("ведите размер списка:\n"))
mas = [ ] #declare list
for i in range (n):
    a = random.randint(1,100)
    mas.append(a) #create list
print(mas)

mas_lenght = len(mas) #find lenght list numbers
new_mas = []
for i in range (1 , len(mas) -1 ):
    if mas[i]%2 ==0: #find even number
        b = int(mas[i] + mas[i + 1])
        #print(b)
        new_mas.append(b) #create new list
print(new_mas)
