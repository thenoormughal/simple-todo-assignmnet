# Software Quality Engineering - Assignment 3: Build Unit Test Automation Solution

## Project Overview
This repository contains the complete implementation for Assignment 3. The objective of this project is to set up a Python-based application environment, implement modular components, apply black-box testing techniques (ECP & BVA), write automated unit test cases using `pytest`, integrate data-driven testing via CSV/Excel, and configure parallel execution suites.

---

## Project Structure & Task Breakdown

1. **Task 1: Open-Source Project Setup**
   - Developed a Python Flask-based application structure.
   - Recorded a setup and demonstration video (`setup_demo.mp4` / uploaded to repo)[cite: 1].

2. **Task 2: Automated Unit Test Cases & Testing Notes**
   - Implemented 3 different modules[cite: 1]:
     - `calculator.py` (Arithmetic functions)
     - `app.py` (Flask web routes)
     - `string_utils.py` (String length validation)
   - Applied **Equivalence Class Partitioning (ECP)** and **Boundary Value Analysis (BVA)** documented in `notes.txt`[cite: 1].
   - Created comprehensive automated unit test files (`test_calculator.py`, `test_string_utils.py`) with 5-10 test cases[cite: 1].

3. **Task 3: Test Cases & External Data (Excel & CSV)**
   - Created `Test_Cases.xlsx` containing structured test cases with inputs, expected results, and status[cite: 1].
   - Consumed test data dynamically from an external resource (`test_data.csv`)[cite: 1].

4. **Task 4: Configuration & Parameterization**
   - Configured `pytest.ini` for test grouping, markers, and execution control[cite: 1].
   - Implemented test parameterization (`test_parameterized.py`) to handle data-driven test scenarios[cite: 1].

---

## How to Run the Project & Tests Locally

### 1. Clone the Repository & Setup Virtual Environment
```bash
git clone <repository-url>
cd simple-todo-app
python -m venv venv
2. Activate Virtual Environment
Windows (PowerShell):

Bash
venv\Scripts\Activate.ps1
3. Install Dependencies
Python
pip install Flask pytest
4. Run the Application
Bash
python app.py
5. Run Automated Unit Tests
To execute all test cases using pytest, run:

Bash
pytest -v