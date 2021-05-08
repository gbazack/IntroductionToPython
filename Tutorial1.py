"""
In this tutorial, you will learn how to implement a school management system with Python data structures such as list and dictionary and interact with it via functions.
@gbazack, Jan 2021
""""

#Create a database to save students
student=dict(ID=[1, 2], names=["Joel Ndoumbe", "Paule Hadja"], age=[1,2], level=["Master", "Master"], sex=["Male", "Female"])
#Create a database to save teacher.
teacher={'ID': [1], 'names':["Edinio Zacko"], 'age':[30], 'sex':["Male"], 'courseID':[1]}
#Create a database to register courses.
course={'ID':[1, 2], 'names':["Python programming", "Machine Learning"], 'category':["Computer Science", "Mathematics"], 'teacherID':[1,1]}
#Create a database to save the notes.
note={'ID':[1, 2, 3, 4], 'studentID':[1,2,1,2], 'courseID':[1,1,2,2], 'values':[60, 60, 50, 50]}

#Search items from databases
def getID(Name, database):
#this function finds and returns ID of items from student, teacher and course databases
   for index in range(len(database['names'])):
      if Name in database['names'][index]:
         return database['ID'][index]
         break
   return -1

def getNote(Name, courseTitle):         
   studentID= getID(Name, student)
   courseID= getID(courseTitle, course)
   
   for index in range(len(note['ID'])):
      if note['studentID'][index]==studentID and note['courseID'][index]==courseID:
            return note['values'][index]
            break
   return -1

#Add items to student database
def AddStudent(*args):
   student['ID'].append(len(student['ID'])+1)
   student['names'].append(args[0])
   student['age'].append(args[1])
   student['level'].append(args[2])
   student['sex'].append(args[3])

#Remove items from student database
def RemoveStudent(Name):
   studentID= getID(Name, student)
   student['ID'].remove(studentID)
   student['names'].remove(student['names'][studentID-1])
   student['age'].remove(student['age'][studentID-1])
   student['level'].remove(student['level'][studentID-1])
   student['sex'].remove(student['sex'][studentID-1])

#Modify items of student database
def setNote(Name, courseTitle, Value):
   studentID= getID(Name, student)
   courseID= getID(courseTitle, course)
   
   for index in range(len(note['ID'])):
      if note['studentID'][index]==studentID and note['courseID'][index]==courseID:
         note['values'][index]= Value
      
