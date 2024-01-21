def inputNumOf(args): 
        Num = input("Enter the number of " + args + "(s) to add in this class: ")
        return Num

def showStudents(students):
    if len(students) == 0:          #check students arr
            print("There aren't any students yet")
            return
    print("Here is the students list: ")
    print("-------------------------------------------------")
    for student in students:
        print(f"{student.getId()} - {student.getName()} - {student.getDob()}")
        print("-------------------------------------------------")

def showCourses(courses):
    if len(courses) == 0:          #check courses dict
        print("There aren't any courses yet")
        return
    print("Here is the courses list: ")
    print("-------------------------------------------------")
    for couId, course in courses.items():
        print(f"{course.getId()} - {course.getName()}")
        course.showMarks()
        print("-------------------------------------------------")

class Student():
    def __init__(self, id, name, dob):
        self.__id = id
        self.__name = name
        self.__dob = dob

    #Encapsulation
    def getId(self):
        return self.__id
    
    def getName(self):
        return self.__name
    
    def getDob(self):
        return self.__dob        
    
class Course:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name
        self.__marks = {}

    #Encapsulation
    def getId(self):
        return self.__id
    
    def getName(self):
        return self.__name
    
    def getMarks(self):
        return self.__marks
    
    def addMark(self, students):
        stuId = input("Enter the student's id to add mark: ")
        while stuId not in [student.getId() for student in students]:           #check find student
            stuId = input("The student does not exist! Enter again: ")
        else:
            mark = input("Enter the mark: ")
            while mark.isnumeric() == False:
                mark = input("Invalid mark! Enter the mark again: ")
            else:
                self.getMarks().update({stuId: float(mark)})

    def showMarks(self):
        if len(self.getMarks()) == 0:
            print("This course has no mark")
        else:
            for stuName, mark in self.getMarks().items():
                print(f"\t{stuName}: {mark}")
    
class Class:
    def __init__(self):
        self.__students = []
        self.__courses = {}
    
    #Encapsulation
    def getStudents(self):
        return self.__students
    
    def getCourses(self):
        return self.__courses
    
    def addStudents(self, student):
        self.__students.append(student)

    def addCourses(self, course):
        self.__courses.update(course)

def main():
    myClass = Class()
    myClass.addStudents(Student("22BI13437","Trung","27-02-2004"))
    myClass.addStudents(Student("22BI12360","Vy","26-10-2003"))
    myCou1 = Course("ICT001", "ADS")
    myCou2 = Course("ICT002", "OOP")
    myCourses = {myCou1.getId():myCou1,
                 myCou2.getId():myCou2}
    myClass.addCourses(myCourses)
    
    while(True):
        print("""
=========================================================================
        0. Exit
        1. Add student(s) to the class.
        2. Add course(s) into the class.
        3. Input mark for student in a course. 
        4. List students.
        5. List courses and their marks
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
                    id = input("Enter the student's id: ")
                    name = input("Enter the student's name: ")
                    dob = input("Enter the student's date of birth (dd-mm-yy): ")   
                    myStudent = Student(id, name, dob)                                                                                                                   
                    myClass.addStudents(myStudent)
                    stuNum -= 1

        elif option == 2:
            couNum = inputNumOf("course")
            while couNum.isnumeric() == False:
                couNum = input("Invalid number of course(s). Enter again: ")
            else:
                print("There are " +couNum + " course(s) ready to be added")
                couNum = int (couNum)
                while couNum > 0:
                    print("""
------------------------------------------------------------
                          """)
                    id = input("Enter the course's id: ")
                    name = input("Enter the course's name: ")
                    newCourse = Course(id, name)
                    myCourses.update({id:newCourse})
                    myClass.addCourses(myCourses)
                    couNum -= 1

        elif option == 3:
            couId = input("Enter the id of the course to input marks for: ")
            while couId not in myCourses.keys():            #check find course
                couId = input(("The course does not exist! Enter again: "))
            else:
                tempCou = myCourses[couId]   
                tempCou.addMark(myClass.getStudents())

        elif option == 4:
            showStudents(myClass.getStudents()) 

        elif option == 5:
            showCourses(myClass.getCourses())

if __name__ == "__main__":
    main()