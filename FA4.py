noofstudents = int(input("Enter the number of students: "))
noofsubjects = int(input("Enter the number of subjects: "))

classscore = 0

for student in range(1, noofstudents+1):
    print("Student: ", student)
    studentscore = 0
    
    for subject in range(1, noofsubjects+1):
        score = float(input("Enter score: "))
        studentscore += score
    
    studentaverage = studentscore / noofsubjects
    print("Student average is", studentaverage)
    classscore += studentaverage
 
classaverage = classscore / noofstudents
print("Class average is", classaverage)
