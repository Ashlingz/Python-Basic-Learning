class cal:
    no = None
    __num = None

    def __init(self,no,num,):
        self.num = num
        self.__no = no

    def __str(self):
        return f'No: {self.no} \n'\
                f'Number: {self.__num}'

    def getNum(self):
        return self.__num

    def getNo(self):
        return  self.__no

    def __add(self, other):
        new_no = self.no, other.getNo()
        new_num = self.__num+other.getNum()

        return f'No: {new_no}\n'\
                f'Number: {new_num}'

    def __sub(self, other):
        new_no = self.no, other.getNo()
        new_num = self.__num-other.getNum()

        return f'No: {new_no}\n'\
                f'Number: {new_num}'

    def __mul(self, other):
        new_no = self.no, other.getNo()
        new_num = self.__num*other.getNum()

        return f'No: {new_no}\n'\
                f'Number: {new_num}'

    def __truediv(self, other):
        new_no = self.no, other.getNo()
        new_num = self.__num / other.getNum()

        return f'No: {new_no}\n' \
               f'Number: {new_num}'

    def __gt(self, other):
        if self.num > other.getNum():
            return f'{self.__num} is greater than {other.getNum()}'
        else:
            return f'{other.getNum()} is greater than {self.__num}'

    def __lt(self, other):
        if self.num < other.getNum():
            return f'{self.__num} is less than {other.getNum()}'
        else:
            return f'{other.getNum()} is less than {self.__num}'

    def __eq(self, other):
        if self.__num == other.getNum():
            return f'{self.__num} is equal to {other.getNum()}'
        else:
            return f'{self.__num} is not equal to {other.getNum()}'