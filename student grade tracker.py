subjects = []
grades = []

num_subjects = int(input("Enter number of subjects: "))

for i in range(num_subjects):
    subject = input(f"Enter subject {i + 1} name: ")
    grade = float(input(f"Enter marks for {subject}: "))

    subjects.append(subject)
    grades.append(grade)

print("\n--- Student Grade Report ---")

for i in range(num_subjects):
    print(f"{subjects[i]}: {grades[i]}")

average = sum(grades) / len(grades)

print(f"\nAverage Marks: {average:.2f}")

if average >= 90:
    print("Grade: A+")
elif average >= 80:
    print("Grade: A")
elif average >= 70:
    print("Grade: B")
elif average >= 60:
    print("Grade: C")
elif average >= 50:
    print("Grade: D")
else:
    print("Grade: F")