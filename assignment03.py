assignments = ["Python", "Maths", "Physics"]

print("Original list:", assignments)

new = input("Enter new assignment: ")
assignments.append(new)

print("After adding:", assignments)

completed = input("Enter completed assignment: ")

if completed in assignments:
    assignments.remove(completed)
else:
    print("Assignment not found")

print("Updated list:", assignments)


