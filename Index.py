print("---STUDENT ORGANAZOR---")


filename = "Students.txt"

try :
    file = open(filename,"r")
    lines = file.readlines()
    file.close()

except FileNotFoundError:
    print("File is not found")
    exit()

class students :
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age 
        self.set_grade(grade)
    def get_grade(self):
        return self.__grade
    def set_grade(self,new_grade):
        if 0 <= new_grade <=20:
            self.__grade = new_grade
        else :
            print("Invalid grade")
            self.__grade = 0 
    def is_passed(self):
        return self.__grade >= 10
    
    def info(self):
        print("Student ",self.name,self.age,self.get_grade())

class excellentStudent(students):
    def is_passed(self):
        return self.get_grade()>= 14

students_list = []
for line in lines :
    parts = line.strip().split(",")
    name = parts[0]
    age = int(parts[1])
    grade = int(parts[2])

    if grade >= 15:
        student=excellentStudent(name,age,grade)
    else:
        student = students(name,age,grade)
    
    students_list.append(student)
    student.info()



students_counts = len(students_list)
print("Number of students:",students_counts)

passed_students_list = []
failed_student_list = []

for student in students_list:
    if student.is_passed():
        passed_students_list.append(student)
        print(f"student {student.name} passed with grade",student.get_grade())

    else: 
        failed_student_list.append(student)
        print(f"Student {student.name} failed with ",student.get_grade())

for student in passed_students_list:
    print("Students that passed: ",student.name,student.age,student.get_grade())

for student in failed_student_list:
    print("Students that failed:",student.name,student.age,student.get_grade())

Oldest = None 
for student in students_list:
    if Oldest is None or Oldest.age < student.age:
        Oldest = student

print("Oldest student is :",Oldest.name," with age ",Oldest.age)


youngest = None 
for student in students_list:
    if youngest is None or youngest.age > student.age :
        youngest = student

print("The youngest student is :",youngest.name,youngest.age)


total = 0 
for student in students_list:
    total += student.age 

print("total is :",total)

if len(students_list) != 0 :
    average= total/len(students_list)
    print(int(average),"is the average ")
else:
    print("No students")