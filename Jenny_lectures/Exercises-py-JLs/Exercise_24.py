student_data=[
    {
        'Name':'Neeraj',
        'Roll_no':196,
        'Age':20,
        'Course':'CSE'
    },
    {
        'Name':'Stuart',
        'Roll_no':187,
        'Age':19,
        'Course':'CSE'
    }
]

def add_new_student(Name,Roll_no,Age,Course):
    new_student={}
    new_student['Name']=Name
    new_student['Roll_no']=Roll_no
    new_student['Age']=Age
    new_student['Course']=Course
    student_data.append(new_student)

add_new_student('Hemanth',287,20,'ECE')    

print(student_data)