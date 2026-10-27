"""
Week 4 Task: Debugging and Optimization
Example project: Student Marks Analyzer

This program validates student marks, calculates an average, assigns a grade,
and reports the result. It demonstrates defensive input handling and clear
function design.
"""

def get_mark(subject: str) -> float:
    """Read and validate a mark from 0 to 100."""
    while True:
        raw_value = input(f"Enter marks for {subject} (0-100): ").strip()
        try:
            mark = float(raw_value)
        except ValueError:
            print("Invalid input. Please enter a number, such as 78 or 82.5.")
            continue

        if 0 <= mark <= 100:
            return mark

        print("Marks must be between 0 and 100. Please try again.")


def calculate_average(marks: list[float]) -> float:
    """Return the arithmetic mean of a non-empty list of marks."""
    if not marks:
        raise ValueError("At least one mark is required.")
    return sum(marks) / len(marks)


def assign_grade(average: float) -> str:
    """Assign a grade using descending thresholds."""
    if average >= 90:
        return "A"
    if average >= 80:
        return "B"
    if average >= 70:
        return "C"
    if average >= 60:
        return "D"
    return "F"


def main() -> None:
    subjects = ("Maths", "Science", "English")
    marks = [get_mark(subject) for subject in subjects]

    average = calculate_average(marks)
    grade = assign_grade(average)

    print("\n--- Student Results ---")
    print(f"Marks: {', '.join(f'{mark:g}' for mark in marks)}")
    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}")

    if all(mark >= 40 for mark in marks):
        print("Status: Passed every subject.")
    else:
        print("Status: Needs improvement in at least one subject.")


if __name__ == "__main__":
    main()
