# a = 0
# b = 1

# try:
#     c = a / b
#     print(f'{c}')
# except ZeroDivisionError as err:
#     print(err)
#     print('Error Cannot Divide')
# else:
#     print('Error While Proccessing')
# # fianlly can go to all condition. try/except/else
# finally:
#     print()

# while True:
#     value = input('Enter Number: ')
#     try:
#         value = int(value)
#     except ValueError:
#         print('Please Enter Number')
#         continue
#     if 1 <= value <= 100:
#         print(f'Your Value is Pass {value}')
#         break
#     else:
#         print('Please Input Again')

def contains_number(string):
    return any(char.isdigit() for char in string)



while True:
    print('--------------------------------------------')
    name = input('Enter Your Username:')
    try:
        if contains_number(name) == False:
            name = str(name)
        else:
            name = int(name)
    except Exception as e:
        print('Please Ensure Your Username Have no Number')
        print(e)
        continue
    # if contains_number(name):
    #     print('Please Ensure Your Username Have no Number')
    #     continue
    else:
        print(f'Your Name is {name}')
        break
   


