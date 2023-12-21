import os


def write_data_to_file(data):
    with open('data.txt', 'a') as file:
        for user in data:
            file.write(f"{user['name']},{user['gender']},{user['age']}\n")


def read_data_from_file():
    data = []
    with open('data.txt', 'r') as file:
        for line in file:
            name, gender, age = line.strip().split(',')
            user = {
                'name': name,
                'gender': gender,
                'age': age
            }
            data.append(user)
    return data


def main():
    user_data = []
    id = ""
    print("Input 1 to Rigistering")
    print("Input 2 to Show List")
    print("Input 3 to Clear Screen")
    print("Input 4 to Exit the Terminal")
    print("---------------------------------------------------")
    while True:
        id = input("Enter Number:")
        if id == '1':
            name = input("Enter Name: ")
            gender = input("Enter gender: ")
            age = input("Enter age: ")
            print("---------------------------------------------------")
            user = {
                'name': name,
                'gender': gender,
                'age': age
            }

            user_data.append(user)

            write_data_to_file(user_data)
            print("Data written to file.")
            # stored_data = read_data_from_file()

        elif id == '2':
            stored_data = read_data_from_file()
            print("Name\tGender\tAge")
            for user in stored_data:
                print(f"{user['name']}\t {user['gender']}\t{user['age']}")

            print("---------------------------------------------------")
        elif id == '3':
            os.system('cls')
            print("Input 1 to Rigistering")
            print("Input 2 to Show List")
            print("Input 3 to Clear Screen")
            print("Input 4 to Exit the Terminal")
            print("---------------------------------------------------")

        elif id == '4':
            break
        else:
            print("Number Input does not Exist, Please Input The Exist Number Above")
            print("---------------------------------------------------")
            continue


if __name__ == '__main__':
    main()
