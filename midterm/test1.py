class UserSystem:
    list = []
    name = ""
    age = 0
    gender = ""

    def __init__(this) -> None:
        pass

    def inputInfo(this):
        this.name = input("Enter Name: ")
        this.age = input("Enter Age: ")
        this.gender = input("Choose Gender: ")

    def show(this):
        print("Name: " + this.name)
        print("Age: " + str(this.age))
        print("Gender: " + this.gender)


class Run:
    b = UserSystem()
    print("Menu")

    x = 0

    while(x != 10):

        x = input("Enter: ")
        
                 
    
