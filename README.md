# Survey Data Analysis

This repository contains Python code for analyzing survey data using the pandas library. The code processes survey data stored in an Excel file format and performs various data manipulation and analysis tasks. The resulting cleaned and analyzed data is then exported to a new Excel file.

## Files

- **survey_analysis.py**: Python script for survey data analysis.
- **Data - Survey Monkey Output edited.xlsx**: Excel file containing the survey data.
- **README.md**: Documentation file (you are reading it).

## Dependencies

- Python 3.x
- pandas library

Install the required dependencies using pip:

```bash
pip install pandas
```

## Usage

1. Place the survey data file (`Data - Survey Monkey Output edited.xlsx`) in the same directory as the `survey_analysis.py` script.
2. Execute the `survey_analysis.py` script using Python.
3. The cleaned and analyzed data will be saved as `Final_Output_Sheet.xlsx` in the same directory.

## Description

The Python script performs the following tasks:

1. Reads the survey data from the Excel file.
2. Cleans the data by dropping unnecessary columns.
3. Unpivots the data to convert it from wide to long format.
4. Merges the unpivoted data with another sheet containing additional information about the survey questions.
5. Calculates the number of respondents for each question.
6. Calculates the number of respondents providing the same answer for each question.
7. Renames the columns for better readability.
8. Exports the final analyzed data to a new Excel file.
