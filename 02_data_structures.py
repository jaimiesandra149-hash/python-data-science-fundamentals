# Lists and Dictionaries

students = ["Aisha", "Rahul", "Priya", "Arun"]

print("Student List:")
for student in students:
    print(student)

student_marks = {
    "Aisha": 85,
    "Rahul": 78,
    "Priya": 92,
    "Arun": 88
}

print("\nStudent Marks:")
for name, mark in student_marks.items():
    print(name, ":", mark)
