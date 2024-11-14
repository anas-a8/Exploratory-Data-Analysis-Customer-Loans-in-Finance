# Data Analysis Project - Loan Payment Analysis

## Table of Contents
1. [Project Description](#project-description)
2. [Aim of the Project](#aim-of-the-project)
3. [What I Learned](#what-i-learned)
4. [Installation Instructions](#installation-instructions)
5. [Usage Instructions](#usage-instructions)
6. [File Structure](#file-structure)
7. [License](#license)

## Project Description
This project aims to analyze loan payment data using Python and various data analysis techniques. The data is cleaned, transformed, and visualized to derive insights about loan repayment, defaults, and the factors influencing loan defaults. The analysis is done using Jupyter notebooks (.ipynb files) and Python scripts.

This project helps identify patterns in loan repayment behavior by analyzing features such as interest rate, loan grade, and purpose. Furthermore, we assess the financial impact of loans marked as "Charged Off" and determine indicators that could help predict loan defaults in the future.

## Aim of the Project
The goal of the project is to:
- Clean and transform loan data to prepare it for analysis.
- Identify insights into the factors contributing to loan repayments and defaults.
- Visualize loan repayment trends and analyze key metrics.
- Create a reproducible data analysis pipeline using Python and Jupyter notebooks.

## What I Learned
- Data cleaning and transformation using pandas.
- How to create reusable classes to perform data transformation, impute missing values, and visualize data.
- How to identify skewed data, handle outliers, and perform correlation analysis.
- Techniques to visualize data effectively for drawing meaningful insights.

## Installation Instructions
1. **Clone the Repository**:
   ```sh
   git clone https://github.com/username/repo.git
   ```

2. **Navigate to the Project Directory**:
   ```sh
   cd data-analysis-project
   ```

3. **Install Dependencies**:
   You will need Python 3.8 or later. Create a virtual environment and install the dependencies from `requirements.txt`:
   ```sh
   python -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   pip install -r requirements.txt
   ```

## Usage Instructions
1. **Run the Jupyter Notebooks**:
   - Start the Jupyter server:
     ```sh
     jupyter notebook
     ```
   - Open `analysis_milestone.ipynb` or `main.ipynb` to run the analysis.

2. **Data Transformation**:
   - The data transformation methods are implemented in `data_transform.py`.
   - You can import the `DataTransform` and `DataFrameInfo` classes from `data_transform.py` for any transformations or data exploration.

3. **Visualizations**:
   - The visualization methods are implemented in `plotter.py`.
   - You can use the `Plotter` class to create various plots to analyze data insights.

## File Structure
- `analysis_milestone.ipynb`: A Jupyter notebook that contains the milestone analysis.
- `main.ipynb`: A Jupyter notebook that combines all steps in the project.
- `data_transform.py`: Python script for the `DataTransform` and `DataFrameInfo` classes for handling data transformations and analysis.
- `plotter.py`: Python script for the `Plotter` class used to visualize data insights.
- `loan_payments_cleaned.csv`: Cleaned dataset used in the analysis.
- `README.md`: Information about the project, instructions for installation and use, and a summary of what was done.
- `.venv/`: Virtual environment for managing dependencies.
- `requirements.txt`: File listing all dependencies needed for the project.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

