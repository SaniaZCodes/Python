id_101={
    "Name":"Sania Zafar",
    "Courses":["OOP","Pre Calculus II","Technical and Business Writing","Python"]
}

id_102={
    "Name":"Muhammad Ali",
    "Courses":["Statistic and Probability","Operating Research","Human Computer Interaction","Logic"]
}

id_103={
    "Name":"Ayesha Umair",
    "Courses":["AI","Discrete","Compiler Construction","Python"]
}

id_104={
    "Name":"Hamza Khan",
    "Courses":["Web Development","Opearting System","Expository Writing","Data Structures"]
}

student_db={
    101:id_101,
    102:id_102,
    103:id_103,
    104:id_104
}

#tuple
core_requirements=("Python", "Data Structures", "Logic")

#list
requested_electives=["AI", "Graphics", "AI", "Web", "Graphics"]

# set
unique_electives=set(requested_electives)

#The Operations (Logic):

student_db[105]={"Name":"Hassan Ali", "Courses":["Python","App","Foraml Research"]}

student_db[101]["Courses"].append("Machine Learning")

if "Python"  in  core_requirements:
    print("Yes, 'Python' is present in the core requirment subjects.")

for studentId, info in student_db.items():
    name=info["Name"]
    primary_course=info["Courses"][0]
    print(f"Student ID: {studentId} | Name: {name} | Primary Course: {primary_course}")
