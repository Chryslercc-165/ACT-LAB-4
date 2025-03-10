def assign_grade():
    while True:
        marks = int(input("Enter score (or type -1 to exit): "))  

        if marks == -1:
            print("Goodbye!")
            break  

        if marks < 0 or marks > 100:
            print("Invalid score! Enter a value between 0 and 100.")
        elif marks >= 90:
            print("Grade: A")
        elif marks >= 80:
            print("Grade: B")
        elif marks >= 70:
            print("Grade: C")
        elif marks >= 60:
            print("Grade: D")
        else:
            print("Grade: F")

assign_grade()