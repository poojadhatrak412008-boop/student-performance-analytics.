# Project Documentation: Student Performance Analytics System

## 1. Project Title
**Student Performance Analytics System**

**Student:** Dhatrak Pooja Ganesh  
**Course:** Python with AI  
**Branch:** B.E. Automation and Robotics Engineering  
**College:** Pravara Rural Engineering College, Loni

## 2. Objective
The objective is to build a simple Python-based system that organizes student marks and attendance and turns the data into useful academic summaries. It reduces repetitive manual calculations and helps identify subject-wise performance and top performers.

## 3. Technologies Used
- **Python:** program logic, conditions, loops and reusable functions.
- **Pandas:** reads CSV data into a DataFrame, organizes records and summarizes subject averages.
- **NumPy:** calculates totals and average marks using numerical array operations.
- **CSV:** stores the sample student dataset.

## 4. Dataset Description
The sample dataset contains 20 fictional student records. The columns are:
- `Student_ID`: unique student number
- `Name`: student name
- `Department`: department name
- `Python`, `Mathematics`, `Electronics`, `Communication`: marks out of 100
- `Attendance_Percent`: attendance percentage

The sample names and scores are illustrative. Use approved real data only if permitted by the trainer.

## 5. Implementation
1. The program reads `students.csv` with `pandas.read_csv()`.
2. It checks that the required columns exist and that the dataset is not empty.
3. It converts the subject marks to a NumPy array.
4. NumPy calculates total marks and average marks for each student.
5. A reusable `assign_grade()` function assigns a grade based on the average.
6. A loop checks whether each subject mark is at least 40. If all subjects meet the threshold, the result is Pass; otherwise, Fail.
7. Pandas summarizes overall class performance and subject-wise averages.
8. The program lists the top three students and saves all calculated results to `analysis_results.csv`.

## 6. Key Features
- Dataset loading and basic validation
- Student total and average calculations
- Grade assignment
- Pass/fail classification
- Class average, highest and lowest average
- Pass/fail counts and average attendance
- Subject-wise average comparison
- Top-three performer identification
- CSV export of analyzed results

## 7. Output / Screenshots
Run `python main.py` and capture screenshots of:
1. Overall class summary
2. Student results table
3. Subject-wise averages and best-performing subject
4. Top-three performers
5. The generated `analysis_results.csv`

Insert the screenshots here before final submission.

## 8. Final Outcome
The project produces a readable summary of student performance from a CSV dataset. It demonstrates the use of Python variables, data types, conditions, loops and functions along with Pandas DataFrames and NumPy numerical calculations.

## 9. Challenges and Learning
- **Challenge:** Keeping data column names consistent.  
  **Learning:** Validate required columns before processing.
- **Challenge:** Calculating results for multiple students.  
  **Learning:** Use NumPy arrays and loops instead of repeating calculations manually.
- **Challenge:** Making results easy to read and reuse.  
  **Learning:** Use Pandas tables and export results to CSV.
- **Challenge:** Defining fair pass/fail and grade rules.  
  **Learning:** Document the rules clearly so results are understandable.

## 10. GitHub Repository
**Repository URL:** Add your own GitHub repository URL here after uploading the project.

## Grading Rules Used
- A+: average >= 90
- A: average >= 80 and < 90
- B: average >= 70 and < 80
- C: average >= 60 and < 70
- D: average >= 50 and < 60
- F: average < 50

A student passes only if they score at least 40 in each of the four subjects. These rules are project assumptions and can be changed if the trainer specifies different rules.
