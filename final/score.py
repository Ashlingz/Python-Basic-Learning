class score:
    __kh = None
    __math = None

    def __init__(self, kh, math):
        self.__kh = kh
        self.__math = math

    def getKh(self, kh):
        return self.__kh

    def getMath(self, math):
        return self.__math

    def __str__(self):
        return f'Khmer:{self.__kh}\t Math:{self.__math}'


    def scoreTotal(self):
        return self.__kh + self.__math

    def getTotal(self):
        return f'Khmer:{self.__kh}\t Math:{self.__math}\nTotal{self.scoreTotal()}'