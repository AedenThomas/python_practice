import numpy as np

# Create an array of 12 students in a 3x4 grid
students = np.array([
    ["Alice", "Bob", "Carol", "Dave"],
    ["Eve", "Frank", "Grace", "Hannah"],
    ["Ivan", "Jenny", "Karen", "Laura"]
])

# Create an array of students from the given array using slicing
selected_students = np.array([
    students[0, 1],  # 2nd Person in the 1st row
    students[1, 3],  # 4th Person in the 2nd row
    students[0, 2]   # 3rd Person in the 1st row
])

# Print the selected students
print(selected_students)
