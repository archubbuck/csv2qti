

import argparse
import os
from secrets import choice
from unicodedata import name

import pandas as pd
from text2qti.config import Config
from text2qti.qti import QTI
from text2qti.quiz import Quiz

from markup import markup_mc, markup_mr
import logging

def main():

    # Create the argument parser

    parser = argparse.ArgumentParser(prog='csv2qti')
    parser.set_defaults(func=lambda x: parser.print_help())
    parser.add_argument('--csv', help='The file path to the CSV document that you would like to convert to QTI format.')
    parser.add_argument('--markup', help='The file path to save the markup document to.')
    parser.add_argument('--qti', help='The file path to save the QTI document to.')
    parser.add_argument('--log', choices=[v for (k, v) in logging._levelToName.items() if type(k) is int], type=str.upper, default=logging.getLevelName(logging.INFO), help='Only use this flag when you are trying to debug an issue with the program.')
    args = parser.parse_args()

    # Configure the logger

    logging.basicConfig(level=logging._nameToLevel[args.log])

    # Resolve the absolute file paths from the argument parser

    csv_file_path = os.path.abspath(args.csv)
    markup_file_path = os.path.abspath(args.markup)
    qti_file_path = os.path.abspath(args.qti)

    # Load the data from the CSV into a Pandas DataFrame for processing

    logging.info(f'Loading CSV data from {csv_file_path}')

    csv_data = pd.read_csv(csv_file_path, encoding="ISO-8859-1", engine="python")

    # Process each row in the Pandas DataFrame and store the results

    quiz_questions = ''

    logging.info(f'Processing CSV data from {csv_file_path}')

    for index, row in csv_data.iterrows():
        logging.debug(index, row)

        question_type = row['Type']

        if question_type == 'MC':
            quiz_questions += markup_mc(index, row) + '\n'

        if question_type == 'MR':
            quiz_questions += markup_mr(index, row) + '\n'

    # Save the markup data to be used in the conversion to QTI format

    logging.info(f'Saving markup data to {markup_file_path}')

    with open(markup_file_path, 'w', encoding="ISO-8859-1") as fh:
        fh.write(quiz_questions)

    # Create the Quiz object using text2qti

    logging.debug(f'Creating the Quiz object using text2qti')

    quiz = Quiz(quiz_questions, config=Config({
        'latex_render_url': 'https://canvas.instructure.com/',
        'pandoc_mathml': False,
        'run_code_blocks': False
    }))

    logging.debug(f'Successfully created the Quiz object using text2qti')

    # Create the QTI object using text2qti

    logging.debug(f'Creating the QTI object using text2qti')

    qti = QTI(quiz)

    logging.debug(f'Successfully created the QTI object using text2qti')

    # Save the QTI data

    logging.debug(f'Saving the QTI data to {qti_file_path}')

    qti.save(qti_file_path)

    logging.info(f'Successfully saved the QTI data to {qti_file_path}')

if __name__ == "__main__":
    main()