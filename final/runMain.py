from student import *

s1 = student('Ranny', 21, 'M', 45, 45)
s2 = student('Lyma', 22, 'F', 55, 55)
s3 = student('SangChi', 23, 'M', 65, 65)

# Inheritance
print('Inheritance')
print('--------------------------------------')
print(s1)

# Encapsulation
print('Encapsulation')
print('--------------------------------------')
print(s1.getInfo())

# Polymorphism
print('Polymorphism')
print('--------------------------------------')
s1 = s2
print(s1)