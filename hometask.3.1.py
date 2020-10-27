"""
#Создать класс Student: id, Фамилия, Имя,  Отчество, Дата рождения, Адрес, Телефон, Факультет, Курс, Группа.
#Функции-члены реализуют запись и считывание полей (проверка корректности), расчет возраста студента
#Создать список объектов. Вывести:
#a) список студентов заданного факультета;
#d) список учебной группы.
"""
from datetime import date, datetime


class Student:
    def __init__(self, id, fullname, name, suname, adress, phone, faculty, cours, group ):

        self.id = id
        self.fullname = fullname
        self.name     = name
        self.suname   = suname
        self.adress   = adress
        self.phone    = phone
        self.faculty  = faculty
        self.cours    = cours
        self.group    = group
        #self.birthDate = birthDate

        def get_faculty(self):
            return self.faculty

        def get_group(self):
            return self.group

        def calculateAge(self, age):
            today = date.today()
            birthDate = date(2019, 9, 21)
            age = today.year - birthDate.year
            if (today.month < birthDate.month or (today.month == birthDate.month and today.day < birthDate.day)):
                age = age - 1

            return age

            """
            return str(self.id) + " " + str(self.fullname) + " " + str(self.name) + ", " \
               + ", " + str(self.suname) + " " + str(self.adress) + ", " + str(self.phone) \
               + ", " + str(self.faculty) + ", " + str(self.cours)  + ", " + str(self.group) 
            """

            print(age)

students_list = [Student("01","Nazarchuk", "Dzmitry", "Sergeevich", "Misk", "+37529xxxxxx", "economic", 5, 107,)]

