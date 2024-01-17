#Input number of (students/courses) to add in the class
def inputNumOf(args): 
    Num = input("Enter the number of " + args + "(s) to add in this class: ")
    return Num

#Information of students and courses using dict
def inputInfo(args):
    student = {
        f"{args[0]}":{
            "name":args[1],
            "dob":args[2]
        }
    }
    return student

def inputCourse(args):
    course = {
        f"{args[0]}":args[1]
    }
    return course

def inputMark(students, courses):
    stuId = input("Enter the student id to add mark: ")
    if stuId not in students:
        print("The student does not exist!")
    else:
        couId = input("Enter the course id to add mark: ")
        if couId not in courses:
            print("The course does not exist!")
        else:
            mark = input("Enter the mark: ")
            while mark.isnumeric() == False:
                mark = input("Invalid mark! Enter the mark again: ")
            if "marks" not in students[stuId]:
                students[stuId]['marks'] = {}
            if couId not in students[stuId]['marks']:
                students[stuId]['marks'][couId] = []
            students[stuId]['marks'][couId].append(int(mark))
def listStudents(students):
    if len(students) == 0:
        print("There aren't any students yet")
        return
    print("Here is the students list: ")
    print("-------------------------------------------------")
    for stuId in students.keys():
        print(f"{stuId} - {students[stuId]['name']} - {students[stuId]['dob']}")
        if "marks" in students[stuId].keys() and len(students[stuId]['marks']) > 0:
            for couId in students[stuId]['marks'].keys():
                print(f"{couId}: {students[stuId]['marks'][couId]}")
            else:
                print(f"{students[stuId]['name']} has no mark")
        print("-------------------------------------------------")

def listCourses(courses):
    if len(courses) == 0:
        print("There aren't any courses yet")
        return
    print("Here is the course list: ")
    print("-------------------------------------------------")
    for couId, couName in courses.items():
        print(f"{couId} - {couName}")
        print("-------------------------------------------------")
            
def main():
    stuNum = 0
    couNum = 0
    # Initialize the dict of students and courses
    students = {}
    courses = {}
    
    while(True):
        print("""
=========================================================================
        0. Exit
        1. Add student(s) to the class.
        2. Add course(s) into the class.
        3. Input mark for student in a course. 
        4. List students and their marks.
        5. List courses.
        """)
        option = input("Your choice: ")
        while option.isnumeric() == False:
            option = input("Invalid choice! Please enter your choice again: ")
        else:
            option = int(option)

        if option == 0:
            break

        elif option == 1: 
            stuNum = inputNumOf("student")
            while stuNum.isnumeric() == False:
                stuNum = input("Invalid number of student(s). Enter again: ")
            else:
                print("There are " + stuNum + " students(s) ready to be added")
                stuNum = int(stuNum)  
                while stuNum>0:             
                    print("""
------------------------------------------------------------
                        """)
                    id = input("Enter the student id: ") 
                    name = input("Enter the student name: ")      
                    dob = input("Enter the date of birth(dd-mm-yyyy): ")                                                                                                                       
                    students.update(inputInfo([id, name, dob]))
                    stuNum -= 1 

        elif option == 2:
            couNum = inputNumOf("course")
            if couNum.isnumeric() == False:
                print("Invalid number of course(s)")
            else:
                print("There are " +couNum + " course(s) ready to be added")
                couNum = int (couNum)
                while couNum > 0:
                    print("""
------------------------------------------------------------
                          """)
                    id = input("Enter the course id: ") 
                    name = input("Enter the course name: ")                                                                                                                             
                    courses.update(inputInfo([id, name]))
                    couNum -= 1

        elif option == 3:
            inputMark(students,courses)

        elif option == 4:
            listStudents(students)
    
        elif option == 5:
            listCourses(courses)

        else:
            option = input("Invalid choice! Please enter your choice again: ")

main()