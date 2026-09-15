# Python Mini Project
# Calculator and Data Processing System

def calculator():
    print("\n===== CALCULATOR =====")

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        print("\nSelect Operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Power")

        choice = input("Enter your choice: ")

        if choice == "1":
            result = num1 + num2
            print("Result:", result)

        elif choice == "2":
            result = num1 - num2
            print("Result:", result)

        elif choice == "3":
            result = num1 * num2
            print("Result:", result)

        elif choice == "4":
            if num2 == 0:
                print("Error: Cannot divide by zero.")
            else:
                result = num1 / num2
                print("Result:", result)

        elif choice == "5":
            if num2 == 0:
                print("Error: Cannot perform modulus by zero.")
            else:
                result = num1 % num2
                print("Result:", result)

        elif choice == "6":
            result = num1 ** num2
            print("Result:", result)

        else:
            print("Invalid choice.")

    except ValueError:
        print("Please enter valid numbers.")


def data_processing():
    print("\n===== DATA PROCESSING =====")

    name = input("Enter student name: ")

    try:
        print("\nEnter marks for 5 subjects:")

        marks = []

        for i in range(5):
            mark = float(input(f"Enter marks for subject {i + 1}: "))

            if mark < 0 or mark > 100:
                print("Marks must be between 0 and 100.")
                return

            marks.append(mark)

        total = sum(marks)
        average = total / len(marks)
        highest = max(marks)
        lowest = min(marks)

        if average >= 75:
            grade = "A"
        elif average >= 60:
            grade = "B"
        elif average >= 50:
            grade = "C"
        elif average >= 40:
            grade = "D"
        else:
            grade = "F"

        if average >= 40:
            result = "PASS"
        else:
            result = "FAIL"

        print("\n===== STUDENT REPORT =====")
        print("Student Name:", name)
        print("Marks:", marks)
        print("Total Marks:", total)
        print("Average:", round(average, 2))
        print("Highest Marks:", highest)
        print("Lowest Marks:", lowest)
        print("Grade:", grade)
        print("Result:", result)

    except ValueError:
        print("Please enter valid marks.")


def main():
    while True:
        print("\n================================")
        print(" PYTHON MINI PROJECT")
        print(" Calculator & Data Processing")
        print("================================")

        print("\n1. Calculator")
        print("2. Data Processing")
        print("3. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            calculator()

        elif choice == "2":
            data_processing()

        elif choice == "3":
            print("Thank you for using the program.")
            break

        else:
            print("Invalid choice. Please try again.")


main()