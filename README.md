# Student Performance Analytics System

## Project overview
A Python data-analysis mini project that reads student records from a CSV file and analyzes marks and attendance using **Pandas** and **NumPy**.

## Features
- Loads and validates student data with Pandas.
- Calculates each student's total and average marks using NumPy.
- Assigns grades using a clearly defined grading scale.
- Identifies pass/fail students (at least 40 marks in every subject).
- Displays class statistics and average attendance.
- Compares average marks by subject.
- Lists the top three students.
- Exports full results to `analysis_results.csv`.

## Technologies
- Python 3.10 or later
- Pandas
- NumPy

## Files
- `main.py` — main program and reusable functions
- `students.csv` — sample dataset with 20 fictional student records
- `requirements.txt` — Python dependencies
- `Project_Documentation.md` — project report

## Setup and run
1. Install Python 3.10 or later.
2. Open a terminal in this folder.
3. Install packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Run:
   ```bash
   python main.py
   ```
5. Check `analysis_results.csv` for the complete analyzed data.

## Grade rules
| Average marks | Grade |
|---|---|
| 90–100 | A+ |
| 80–89.99 | A |
| 70–79.99 | B |
| 60–69.99 | C |
| 50–59.99 | D |
| Below 50 | F |

A student passes only if they score at least 40 marks in **every** subject.

## Dataset note
The included names and marks are fictional sample data for demonstration. Replace them with approved data if your trainer requires your own dataset.

## GitHub
Create a repository named `student-performance-analytics`, upload all project files, and copy the repository URL into your trainer's Google Form. Do not submit a GitHub URL until you have created the repository and uploaded the files.
