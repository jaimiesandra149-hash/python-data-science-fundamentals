# Student Performance Analyzer

students = {
    "Aisha": 85,
    "Rahul": 78,
    "Priya": 92,
    "Arun": 88,
    "Meera": 95
}

def calculate_average(marks):
    return sum(marks) / len(marks)

marks = list(students.values())
average = calculate_average(marks)

top_student = max(students, key=students.get)

print("STUDENT PERFORMANCE ANALYZER")
print("----------------------------")

for name, mark in students.items():
    print(name, ":", mark)

print("\nClass Average:", round(average, 2))
print("Top Performer:", top_student)
print("Highest Mark:", students[top_student])
