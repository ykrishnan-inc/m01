from lessons import math_lesson
from lessons import string_lesson


def main():
    """
        Main menu for the Python basics learning app
    """
    while True:
        print("\nPython Basics Learning App")
        print("1. Math Lesson")
        print("2. String Lesson")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            math_lesson.teach_math()
        elif choice == '2':
            string_lesson.teach_strings()
        elif choice == '3':
            print("Thank you for learning Python!")
            break
        else:
            print("Invalid choice. Please try again.")


# Ensure this is the main program being run
if __name__ == "__main__":
    main()
