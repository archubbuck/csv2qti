# csv2qti - Creates quizzes in QTI format from a formatted CSV file

csv2qti converts formatted CSV files into quizzes in QTI format (version 1.2), which can be imported by Canvas and other educational software.

## Getting Started

1. Install [Python 3.8.5 ](https://www.python.org/ftp/python/3.8.5/python-3.8.5-amd64.exe)
2. Execute the following command to install the required libraries: `pip install -r requirements.txt`
3. Run the following sample command to know it's working: `python app.py --csv data/input/sample.csv --markup data/output/sample.txt --qti data/output/sample.zip`

## CSV File Format

Please review [this sample](/data/input/sample.csv) to understand how to format your CSV file.