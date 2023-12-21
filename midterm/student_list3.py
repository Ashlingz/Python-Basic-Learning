n = int(input("Enter number of student: "))
student_list=[]

name = str(input("Enter Student Name: "))
gender = str(input("Enter Student Gender: "))
skill = str(input("Enter Student Skill: "))

student_list = [
     {'name': 'chai', 'gender': 'male', 'skill': 'python'},
     {'name': 'sopheak', 'gender': 'female', 'skill': 'java'},
     {'name': 'sothea', 'gender': 'male', 'skill': 'HTML'},
 ]

print('Name\t\t gender\t\t skill')
for item in student_list:
    print(item['name']+'\t\t' + item['gender'] + '\t\t' + item['skill'])