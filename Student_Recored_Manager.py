# Student Record Manager

students = []  # list to store student records


# ---------------- MENU ----------------
def displayMenu():
    print("\n----- Student Record Manager -----")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student by ID")
    print("4. Show Statistics")
    print("5. Save to File")
    print("6. Load from File")
    print("7. Exit")


# ---------------- ADD STUDENT ----------------
def addStudent():
    sid = input("Enter Student ID: ")
    name = input("Enter Name: ")
    
    try:
        age = int(input("Enter Age: "))
        marks = float(input("Enter Marks: "))

        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100!")
            return

        student = {
            "id": sid,
            "name": name,
            "age": age,
            "marks": marks
        }

        students.append(student)
        print("Student added successfully!")

    except ValueError:
        print("Invalid input! Please enter correct data types.")


# ---------------- DISPLAY ----------------
def displayStudents():
    if not students:
        print("No records found.")
        return

    print("\n--- Student Records ---")
    for s in students:
        print(f"ID: {s['id']}, Name: {s['name']}, Age: {s['age']}, Marks: {s['marks']}")


# ---------------- SEARCH ----------------
def searchStudent():
    sid = input("Enter Student ID to search: ")

    for s in students:
        if s["id"] == sid:
            print("Student Found:")
            print(f"ID: {s['id']}, Name: {s['name']}, Age: {s['age']}, Marks: {s['marks']}")
            return

    print("Student not found.")


# ---------------- STATISTICS ----------------
def calculateStatistics():
    if not students:
        print("No data available.")
        return

    marks_list = [s["marks"] for s in students]

    highest = max(marks_list)
    lowest = min(marks_list)
    average = sum(marks_list) / len(marks_list)

    print(f"Highest Marks: {highest}")
    print(f"Lowest Marks: {lowest}")
    print(f"Average Marks: {average:.2f}")


# ---------------- SAVE ----------------
def saveToFile():
    with open("students.txt", "w") as file:
        for s in students:
            file.write(f"{s['id']},{s['name']},{s['age']},{s['marks']}\n")

    print("Data saved to file.")


# ---------------- LOAD ----------------
def loadFromFile():
    global students
    students = []

    try:
        with open("students.txt", "r") as file:
            for line in file:
                sid, name, age, marks = line.strip().split(",")
                students.append({
                    "id": sid,
                    "name": name,
                    "age": int(age),
                    "marks": float(marks)
                })

        print("Data loaded successfully.")

    except FileNotFoundError:
        print("No saved file found.")


# ---------------- MAIN PROGRAM ----------------
def main():
    while True:
        displayMenu()
        choice = input("Enter your choice: ")

        if choice == "1":
            addStudent()
        elif choice == "2":
            displayStudents()
        elif choice == "3":
            searchStudent()
        elif choice == "4":
            calculateStatistics()
        elif choice == "5":
            saveToFile()
        elif choice == "6":
            loadFromFile()
        elif choice == "7":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Try again.")


# Run program
main()