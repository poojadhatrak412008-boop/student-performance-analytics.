"""
Student Performance Analytics System
Python + NumPy + Pandas mini project

Run:
    pip install -r requirements.txt
    python main.py
"""

from pathlib import Path
import numpy as np
import pandas as pd

DATA_FILE = Path(__file__).parent / "students.csv"
SUBJECTS = ["Python", "Mathematics", "Electronics", "Communication"]
PASS_MARK = 40  # A student must score at least 40 in every subject to pass.


def load_data(file_path=DATA_FILE):
    """Load student records from a CSV file and validate required columns."""
    data = pd.read_csv(file_path)
    required = ["Student_ID", "Name", "Department", *SUBJECTS, "Attendance_Percent"]
    missing = [column for column in required if column not in data.columns]
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(missing)}")
    if data.empty:
        raise ValueError("The student dataset is empty.")
    return data


def assign_grade(average):
    """Return a grade based on the student's average marks."""
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def calculate_results(data):
    """Create total, average, grade, and pass/fail columns."""
    results = data.copy()
    marks = results[SUBJECTS].to_numpy(dtype=float)

    # NumPy numerical operations
    results["Total_Marks"] = np.sum(marks, axis=1)
    results["Average_Marks"] = np.round(np.mean(marks, axis=1), 2)

    grades = []
    statuses = []
    for _, student in results.iterrows():
        grades.append(assign_grade(student["Average_Marks"]))
        # A student passes only if every subject mark is at least PASS_MARK.
        passed = all(student[subject] >= PASS_MARK for subject in SUBJECTS)
        statuses.append("Pass" if passed else "Fail")

    results["Grade"] = grades
    results["Result"] = statuses
    return results


def show_overall_summary(results):
    """Display class-level statistics."""
    print("\n" + "=" * 66)
    print("          STUDENT PERFORMANCE ANALYTICS SYSTEM")
    print("=" * 66)
    print(f"Number of students : {len(results)}")
    print(f"Class average      : {results['Average_Marks'].mean():.2f}%")
    print(f"Highest average    : {results['Average_Marks'].max():.2f}%")
    print(f"Lowest average     : {results['Average_Marks'].min():.2f}%")
    print(f"Students passed    : {(results['Result'] == 'Pass').sum()}")
    print(f"Students failed    : {(results['Result'] == 'Fail').sum()}")
    print(f"Average attendance : {results['Attendance_Percent'].mean():.2f}%")
    print("-" * 66)


def show_student_results(results):
    """Display each student's calculated result."""
    view = results[[
        "Student_ID", "Name", "Total_Marks", "Average_Marks",
        "Grade", "Result", "Attendance_Percent"
    ]].sort_values("Average_Marks", ascending=False)
    print("\nSTUDENT RESULTS (highest average first)")
    print(view.to_string(index=False))


def show_subject_analysis(results):
    """Compare average marks in each subject."""
    subject_averages = results[SUBJECTS].mean().sort_values(ascending=False)
    print("\nSUBJECT-WISE AVERAGE MARKS")
    for subject, average in subject_averages.items():
        print(f"{subject:<18} {average:.2f}")
    print(f"Best-performing subject: {subject_averages.index[0]} ({subject_averages.iloc[0]:.2f})")


def show_top_performers(results, count=3):
    """Display the top students by average marks."""
    print(f"\nTOP {count} PERFORMERS")
    top = results.nlargest(count, "Average_Marks")[["Name", "Average_Marks", "Grade"]]
    print(top.to_string(index=False))


def save_results(results):
    """Save analyzed results to a new CSV file."""
    output_file = Path(__file__).parent / "analysis_results.csv"
    results.to_csv(output_file, index=False)
    print(f"\nFull analysis saved to: {output_file.name}")


def main():
    try:
        students = load_data()
        results = calculate_results(students)
        show_overall_summary(results)
        show_student_results(results)
        show_subject_analysis(results)
        show_top_performers(results)
        save_results(results)
    except FileNotFoundError:
        print("Error: students.csv was not found. Keep it in the same folder as main.py.")
    except (ValueError, KeyError) as error:
        print(f"Could not process the dataset: {error}")


if __name__ == "__main__":
    main()
