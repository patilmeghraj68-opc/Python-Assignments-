try:
    file = open("sample.txt", "r")

    content = file.read()

    print("File Contents:")
    print(content)

    file.close()

except FileNotFoundError:
    print("File not found!")
