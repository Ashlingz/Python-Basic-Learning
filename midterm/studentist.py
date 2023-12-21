student_list = []
def Register():
        n = int(input("Enter number of student: "))

        for i in range( 0,n):
            name = str(input("Enter student name: "))
            gender = str(input("Enter student gender: "))
            age = str(input("Enter student skill: "))
            student = {
                'name':name,
                'gender':gender,
                'skill':age
            }    
            student_list.append(student)
        
        return student_list

def Display():
        print('Name\tAge\tSkill')
        for item in b:
            print(item['name']+'\t'+ item['gender']+'\t'+item['skill'])



# b = Register()
# b = Display()


