Student_data={
    "shubham":{
        'subject':"math",
        'mark':50
    },
    "kalyani":{
        'subject':"math",
        'mark':35
    },
    "shivani":{
        'subject':"math",
        'mark':21
    },
    "riya":{
        'subject':"math",
        'mark':35
    }
}

Pass_student=[]
Fail_student=[]


for i in Student_data:
    if Student_data[i]['mark'] > 35:
        Pass_student.append(i)
    else:
        Fail_student.append(i)


print(Pass_student)
print(Fail_student)