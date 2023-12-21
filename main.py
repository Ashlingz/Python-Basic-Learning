# # from People import *
# # from Product import *
# #
# # p = People('Ly', 'Male', '21')
# # p1 = People('Sing', 'Male', '21')
# # print(str(p)+'\n'+str(p1))
# #
# # total = 0
# # list = []
# # n = int(input('Enter Number: '))
# # for i in range(0, n):
# #     id = int(input('Id: '))
# #     name = input('Name:')
# #     price = float(input('Price:'))
# #     qty = float(input('Qty: '))
# #
# #     p = Product(id, name, price, qty)
# #     list.append(p)
# #
# #
# # for product in list:
# #     total += product.amount()
# #     print(product)
# #     print('-----------------------------')
# #
# # print(total)
#

# from Student import *
# from Teacher import *
#
# p = People(1, 'Manet', 1800)
# # s = Student(2, 'Sy', 2002, 'C', 4.5)
# t = Teacher(2, 'Manet', 1998, 'Skill:Sister Yaaaah', 400)
# print(p)
# # print(s)
# print(t)

# code=["PHP","JAVA","C++","C#","C"]
# num=[100,100,200,300,400,200]
# for c in code:
#     print(c+" "*2)
# total=0
# for n in num:
#     total = total+n
# print(str(total))

from Student import *
ss3 = Class('ss', '3', '3', 20)
ss4 = Class('ss', '4', '3', 25)

ss34 = ss3 + ss4
sub = ss3 - ss4
mul = ss3 * ss4
div = ss3 / ss4
less = ss3 < ss4
greater = ss3 > ss4
eq = ss3 == ss4

# print(ss3)
# print(ss4)
print('Plus---------------------')
print(ss34)
print('SubTruck---------------------')
print(sub)
print('Multiply---------------------')
print(mul)
print('Divide---------------------')
print(div)
print('Comparison')
print(less)
print(greater)
print(eq)


# from Teacher import *
#
# t = Teacher(1, 'Manet', 1998, 'Skill: Math', 100)
# t1 = Teacher(2, 'Manet', 1999, 'Skill: Geometry', 200)
# t2 = Teacher(3, 'Manet', 2000, 'Skill: Khmer', 300)
# print(t)
# print(t1)
# print(t2)
