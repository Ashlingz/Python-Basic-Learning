from score import *

class student(score):
        __name = None
        __gender = None
        __age = None

        def __init__(self, name, gender, age, kh, math):
            super(student, self).__init__(kh, math)
            self.__name = name
            self.__age = age
            self.__gender = gender

        def __str__(self):
            return f'Student: {self.__name}\t Age: {self.__age}\t Gender: {self.__gender}\n'+\
                   '--------------------------------\n'+ super().__str__()+\
                    '\n------------------------------------------------------------------------\n'

        def getInfo(self):
            return f'Student: {self.__name}\t Age: {self.__age}\t Gender: {self.__gender}\n' + \
                   '--------------------------------\n' + super().__str__() + \
                   '\n------------------------------------------------------------------------\n'


        def getInfoToal(self):
            return f'Student: {self.__name}\t Age: {self.__age}\t Gender: {self.__gender}\n' + \
                   '--------------------------------\n' + super().getTotal()+ \
                   '\n------------------------------------------------------------------------\n'
