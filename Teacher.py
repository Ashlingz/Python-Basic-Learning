from People import *

class Teacher(People):
    __skill = None
    __salary = None

    def __init__(self, id , name, year_of_birth, skill, salary):
        super(Teacher, self).__init__(id, name, year_of_birth)
        self.__skill = skill
        self.__salary = salary

    def __str__(self):
        return super().__str__()+f'\t{self.__skill}\t{self.__salary}'
