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

#Input mark info into the students dict
def inputMark(students, courses):
    stuId = input("Enter the student's id to add mark: ")
    
    while stuId not in students:           #check find student
        stuId = input("The student does not exist! Enter again: ")
    else:
        couId = input("Enter the course's id to add mark: ")
        while couId not in courses:            #check find course
            couId = input(("The course does not exist! Enter again: "))           
        else:
            mark = input("Enter the mark: ")
            while mark.isnumeric() == False:            #check valid mark
                mark = input("Invalid mark! Enter the mark again: ")
            if "marks" not in students[stuId]:
                students[stuId]["marks"] = {}
            if couId not in students[stuId]["marks"]:
                students[stuId]["marks"][couId] = []
            students[stuId]["marks"][couId].append(int(mark))

#show student info and their marks of each course
def listStudents(students):
    if len(students) == 0:          #check students dict
        print("There aren't any students yet")
        return
    print("Here is the students list: ")
    print("-------------------------------------------------")
    for stuId, stuInfo in students.items():
        print(f"{stuId} - {stuInfo['name']} - {stuInfo['dob']}")
    
        if "marks" in stuInfo and len(stuInfo["marks"]) > 0:
            for couId, marks in stuInfo["marks"].items():
                print(f"{couId}: {marks}")
        else:
            print(f"{stuInfo['name']} has no mark")
    
        print("-------------------------------------------------")

#show all courses
def listCourses(courses):
    if len(courses) == 0:           #check courses dict
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
    students = {
        "22BI13437" : {
            "name" : "Trung",
            "dob" : "27-02-2004"
        },
        "22BI13857" : {
            "name" : "Vy",
            "dob" : "26-12-2003",
            "marks" : {
                "ICT001" : [20]
            }
        }
    }
    courses = {
        "ICT001" : "ADS",
        "ICT002" : "OOP"
    }
    
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
        while option.isnumeric() == False:          #check input option
            option = input("Invalid choice! Please enter your choice again: ")
        else:
            option = int(option)

        if option == 0:
            break

        elif option == 1: 
            stuNum = inputNumOf("student")
            while stuNum.isnumeric() == False:          #check input stuNum 
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
            while couNum.isnumeric() == False:         #check input couNum
                couNum = input("Invalid number of course(s). Enter again: ")
            else:
                print("There are " +couNum + " course(s) ready to be added")
                couNum = int (couNum)
                while couNum > 0:
                    print("""
------------------------------------------------------------
                          """)
                    id = input("Enter the course id: ") 
                    name = input("Enter the course name: ")                                                                                                                             
                    courses.update(inputCourse([id, name]))
                    couNum -= 1

        elif option == 3:
            if len(students) == 0:          #check students dict
               print("There aren't any students yet")
            elif len(courses) == 0:         #check courses dict
                print("There aren't any courses yet")
            else:
                inputMark(students,courses)

        elif option == 4:
            listStudents(students)
    
        elif option == 5:
            listCourses(courses)

if __name__ == "__main__":
    main()