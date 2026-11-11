# Functions and File Handling

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

marks = [85, 78, 92, 88]

average = calculate_average(marks)
print("Average Marks:", average)

with open("sample_data.txt", "w") as file:
    file.write("Python is useful for Data Science.\n")
    file.write("File handling helps store and retrieve data.")

with open("sample_data.txt", "r") as file:
    content = file.read()

print("\nFile Content:")
print(content)
