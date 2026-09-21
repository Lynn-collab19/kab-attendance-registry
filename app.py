from roster import (
    create_student,
    check_in_student,
    todays_attendance
)


def main():
    while True:

        print("\n========================================")
        print("      KAB STUDENT ATTENDANCE REGISTRY")
        print("========================================")
        print("1. Create Student")
        print("2. Check In Student")
        print("3. Today's Attendance")
        print("4. Exit")
        print("========================================")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            create_student()

        elif choice == "2":
            check_in_student()

        elif choice == "3":
            todays_attendance()

        elif choice == "4":
            print("Thank you for using the Attendance Registry.")
            break

        else:
            print("Invalid option. Please choose 1-4.")


if __name__ == "__main__":
    main()