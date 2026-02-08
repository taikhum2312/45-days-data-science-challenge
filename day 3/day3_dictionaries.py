##Word Frequency WITH Manual Trace
# def word_frequency(sentence=input("enter a string")):
#     frequency={}
#     for word in sentence.lower().split():
#         if word in frequency:
#             frequency[word]+=1
#         else:
#             frequency[word]=1
#         print("word:", word, "frequency:", frequency)
# word_frequency()




## nested dictionary control
students={
    "Taikhum": {"age":19, "maths": 85, "english":92, "science" : 89},
    "Aisha": {"age":20, "maths": 90, "english":88, "science" : 91},
    "Ali": {"age":18, "maths": 78, "english":85, "science" : 80}
    
}


#Calculate Total Marks Per Student with using nested loop
for student, details in students.items():
    total_marks=0
    for subject, marks in details.items():
        if subject != "age":
            total_marks+=marks
    print(f"{student}'s Total Marks: {total_marks}")
    

#Find Top Student
top_student=""
highest_marks=0

for student, details in students.items():
    total_marks=0
    for subject, marks in details.items():
        if subject != "age":
            total_marks+=marks
    if total_marks > highest_marks:
        highest_marks=total_marks
        top_student=student
print(f"Top Student: {top_student} with {highest_marks} marks")