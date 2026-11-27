n = int(input("Enter number of students: "))

if n <= 0:
    print("Number of students must be positive")
else:
    class_total = 0

    for i in range(n):
        print("Student", i + 1)
        total = 0

        for j in range(5):
            marks = float(input("Enter test marks: "))
            total += marks

        average = total / 5
        print("Average marks:", average)
        class_total += total

    overall = class_total / (n * 5)
    print("Class average:", overall)

