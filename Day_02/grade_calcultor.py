# Grade Calculator Script

while True:
    # Ask for student's name
    name = input("Enter the student's name (or 'Exit' to quit): ")
    
    if name.lower() == "exit":
        break
    
    # Ask for 3 subject marks
    marks = []
    for i in range(3):
        mark = float(input(f"Enter mark for subject {i+1}: "))
        marks.append(mark)
    
    # Calculate the average
    average = sum(marks) / 3
    
    # Determine the grade
    if average >= 75:
        grade = "A"
    elif average >= 60:
        grade = "B"
    elif average >= 40:
        grade = "C"
    else:
        grade = "Fail"
    
    # Display the result
    print(f"{name} has achieved Grade {grade} with an average of {average:.2f}")
    print()  # Blank line for separation
