import pandas as pd


def markup_mc(index: int, row: pd.Series):

    markup_question_title_or_id = row['Title/ID']
    markup_question_points = row['Points']
    markup_question_number = index + 1
    markup_question_wording = row['Question Wording']
    markup_question_general_feedback = row['General Feedback']
    markup_question_correct_answer_feedback = row['Correct Feedback']
    markup_question_incorrect_answer_feedback = row['Incorrect Feedback']
    question_correct_answer = row['Correct Answer']
    markup_question_choice_1 = row['Choice 1']
    markup_question_choice_2 = row['Choice 2']
    markup_question_choice_3 = row['Choice 3']
    markup_question_choice_4 = row['Choice 4']
    markup_question_choice_5 = row['Choice 5']
    markup_question_choice_6 = row['Choice 6']
    markup_question_choice_7 = row['Choice 7']
    markup_question_choice_8 = row['Choice 8']
    markup_question_choice_9 = row['Choice 9']
    markup_question_choice_10 = row['Choice 10']

    markup_question_feedback_1 = row['Feedback 1']
    markup_question_feedback_2 = row['Feedback 2']
    markup_question_feedback_3 = row['Feedback 3']
    markup_question_feedback_4 = row['Feedback 4']
    markup_question_feedback_5 = row['Feedback 5']
    markup_question_feedback_6 = row['Feedback 6']
    markup_question_feedback_7 = row['Feedback 7']
    markup_question_feedback_8 = row['Feedback 8']
    markup_question_feedback_9 = row['Feedback 9']
    markup_question_feedback_10 = row['Feedback 10']

    # Title
    question_markup  = f'Title: {markup_question_title_or_id}\n' if pd.notnull(markup_question_title_or_id) else ''

    # Points
    question_markup += f'Points: {markup_question_points}\n' if pd.notnull(markup_question_points) else ''

    # Question Number & Question Wording
    question_markup += f'{markup_question_number}. {markup_question_wording}\n' if pd.notnull(markup_question_wording) else ''

    # General Feedback
    question_markup += f'... {markup_question_general_feedback}\n' if pd.notnull(markup_question_general_feedback) else ''

    # Correct Answer Feedback
    question_markup += f'+   {markup_question_correct_answer_feedback}\n' if pd.notnull(markup_question_correct_answer_feedback) else ''

    # Incorrect Answer Feedback
    question_markup += f'-   {markup_question_incorrect_answer_feedback}\n' if pd.notnull(markup_question_incorrect_answer_feedback) else ''

    # Choice 1
    if pd.notnull(markup_question_choice_1):
        markup_question_choice_1_prefix = f'{"*" if question_correct_answer == markup_question_choice_1 else ""}a)'
        question_markup += f'{markup_question_choice_1_prefix} {markup_question_choice_1}\n'
        if pd.notnull(markup_question_feedback_1):
            question_markup += f'... {markup_question_feedback_1}\n'

    # Choice 2
    if pd.notnull(markup_question_choice_2):
        markup_question_choice_2_prefix = f'{"*" if question_correct_answer == markup_question_choice_2 else ""}b)'
        question_markup += f'{markup_question_choice_2_prefix} {markup_question_choice_2}\n'
        if pd.notnull(markup_question_feedback_2):
            question_markup += f'... {markup_question_feedback_2}\n'

    # Choice 3
    if pd.notnull(markup_question_choice_3):
        markup_question_choice_3_prefix = f'{"*" if question_correct_answer == markup_question_choice_3 else ""}c)'
        question_markup += f'{markup_question_choice_3_prefix} {markup_question_choice_3}\n'
        if pd.notnull(markup_question_feedback_3):
            question_markup += f'... {markup_question_feedback_3}\n'

    # Choice 4
    if pd.notnull(markup_question_choice_4):
        markup_question_choice_4_prefix = f'{"*" if question_correct_answer == markup_question_choice_4 else ""}d)'
        question_markup += f'{markup_question_choice_4_prefix} {markup_question_choice_4}\n'
        if pd.notnull(markup_question_feedback_4):
            question_markup += f'... {markup_question_feedback_4}\n'

    # Choice 5
    if pd.notnull(markup_question_choice_5):
        markup_question_choice_5_prefix = f'{"*" if question_correct_answer == markup_question_choice_5 else ""}e)'
        question_markup += f'{markup_question_choice_5_prefix} {markup_question_choice_5}\n'
        if pd.notnull(markup_question_feedback_5):
            question_markup += f'... {markup_question_feedback_5}\n'

    # Choice 6
    if pd.notnull(markup_question_choice_6):
        markup_question_choice_6_prefix = f'{"*" if question_correct_answer == markup_question_choice_6 else ""}f)'
        question_markup += f'{markup_question_choice_6_prefix} {markup_question_choice_6}\n'
        if pd.notnull(markup_question_feedback_6):
            question_markup += f'... {markup_question_feedback_6}\n'

    # Choice 7
    if pd.notnull(markup_question_choice_7):
        markup_question_choice_7_prefix = f'{"*" if question_correct_answer == markup_question_choice_7 else ""}g)'
        question_markup += f'{markup_question_choice_7_prefix} {markup_question_choice_7}\n'
        if pd.notnull(markup_question_feedback_7):
            question_markup += f'... {markup_question_feedback_7}\n'

    # Choice 8
    if pd.notnull(markup_question_choice_8):
        markup_question_choice_8_prefix = f'{"*" if question_correct_answer == markup_question_choice_8 else ""}h)'
        question_markup += f'{markup_question_choice_8_prefix} {markup_question_choice_8}\n'
        if pd.notnull(markup_question_feedback_8):
            question_markup += f'... {markup_question_feedback_8}\n'

    # Choice 9
    if pd.notnull(markup_question_choice_9):
        markup_question_choice_9_prefix = f'{"*" if question_correct_answer == markup_question_choice_9 else ""}i)'
        question_markup += f'{markup_question_choice_9_prefix} {markup_question_choice_9}\n'
        if pd.notnull(markup_question_feedback_9):
            question_markup += f'... {markup_question_feedback_9}\n'

    # Choice 10
    if pd.notnull(markup_question_choice_10):
        markup_question_choice_10_prefix = f'{"*" if question_correct_answer == markup_question_choice_10 else ""}j)'
        question_markup += f'{markup_question_choice_10_prefix} {markup_question_choice_10}\n'
        if pd.notnull(markup_question_feedback_10):
            question_markup += f'... {markup_question_feedback_10}\n'

    return question_markup

def markup_mr(index: int, row: pd.Series):
    markup_question_title_or_id = row['Title/ID']
    markup_question_points = row['Points']
    markup_question_number = index + 1
    markup_question_wording = row['Question Wording']
    markup_question_general_feedback = row['General Feedback']
    markup_question_correct_answer_feedback = row['Correct Feedback']
    markup_question_incorrect_answer_feedback = row['Incorrect Feedback']
    question_correct_answers = row['Correct Answer'].split(',')
    markup_question_choice_1 = row['Choice 1']
    markup_question_choice_2 = row['Choice 2']
    markup_question_choice_3 = row['Choice 3']
    markup_question_choice_4 = row['Choice 4']
    markup_question_choice_5 = row['Choice 5']
    markup_question_choice_6 = row['Choice 6']
    markup_question_choice_7 = row['Choice 7']
    markup_question_choice_8 = row['Choice 8']
    markup_question_choice_9 = row['Choice 9']
    markup_question_choice_10 = row['Choice 10']

    markup_question_feedback_1 = row['Feedback 1']
    markup_question_feedback_2 = row['Feedback 2']
    markup_question_feedback_3 = row['Feedback 3']
    markup_question_feedback_4 = row['Feedback 4']
    markup_question_feedback_5 = row['Feedback 5']
    markup_question_feedback_6 = row['Feedback 6']
    markup_question_feedback_7 = row['Feedback 7']
    markup_question_feedback_8 = row['Feedback 8']
    markup_question_feedback_9 = row['Feedback 9']
    markup_question_feedback_10 = row['Feedback 10']

    # Title
    question_markup  = f'Title: {markup_question_title_or_id}\n' if pd.notnull(markup_question_title_or_id) else ''

    # Points
    question_markup += f'Points: {markup_question_points}\n' if pd.notnull(markup_question_points) else ''

    # Question Number & Question Wording
    question_markup += f'{markup_question_number}. {markup_question_wording}\n' if pd.notnull(markup_question_wording) else ''

    # General Feedback
    question_markup += f'... {markup_question_general_feedback}\n' if pd.notnull(markup_question_general_feedback) else ''

    # Correct Answer Feedback
    question_markup += f'+   {markup_question_correct_answer_feedback}\n' if pd.notnull(markup_question_correct_answer_feedback) else ''

    # Incorrect Answer Feedback
    question_markup += f'-   {markup_question_incorrect_answer_feedback}\n' if pd.notnull(markup_question_incorrect_answer_feedback) else ''

    # Choice 1
    if pd.notnull(markup_question_choice_1):
        markup_question_choice_1_prefix = f'[{"*" if markup_question_choice_1 in question_correct_answers else " "}]'
        question_markup += f'{markup_question_choice_1_prefix} {markup_question_choice_1}\n'
        if pd.notnull(markup_question_feedback_1):
            question_markup += f'... {markup_question_feedback_1}\n'

    # Choice 2
    if pd.notnull(markup_question_choice_2):
        markup_question_choice_2_prefix = f'[{"*" if markup_question_choice_2 in question_correct_answers else " "}]'
        question_markup += f'{markup_question_choice_2_prefix} {markup_question_choice_2}\n'
        if pd.notnull(markup_question_feedback_2):
            question_markup += f'... {markup_question_feedback_2}\n'

    # Choice 3
    if pd.notnull(markup_question_choice_3):
        markup_question_choice_3_prefix = f'[{"*" if markup_question_choice_3 in question_correct_answers else " "}]'
        question_markup += f'{markup_question_choice_3_prefix} {markup_question_choice_3}\n'
        if pd.notnull(markup_question_feedback_3):
            question_markup += f'... {markup_question_feedback_3}\n'

    # Choice 4
    if pd.notnull(markup_question_choice_4):
        markup_question_choice_4_prefix = f'[{"*" if markup_question_choice_4 in question_correct_answers else " "}]'
        question_markup += f'{markup_question_choice_4_prefix} {markup_question_choice_4}\n'
        if pd.notnull(markup_question_feedback_4):
            question_markup += f'... {markup_question_feedback_4}\n'

    # Choice 5
    if pd.notnull(markup_question_choice_5):
        markup_question_choice_5_prefix = f'[{"*" if markup_question_choice_5 in question_correct_answers else " "}]'
        question_markup += f'{markup_question_choice_5_prefix} {markup_question_choice_5}\n'
        if pd.notnull(markup_question_feedback_5):
            question_markup += f'... {markup_question_feedback_5}\n'

    # Choice 6
    if pd.notnull(markup_question_choice_6):
        markup_question_choice_6_prefix = f'[{"*" if markup_question_choice_6 in question_correct_answers else " "}]'
        question_markup += f'{markup_question_choice_6_prefix} {markup_question_choice_6}\n'
        if pd.notnull(markup_question_feedback_6):
            question_markup += f'... {markup_question_feedback_6}\n'

    # Choice 7
    if pd.notnull(markup_question_choice_7):
        markup_question_choice_7_prefix = f'[{"*" if markup_question_choice_7 in question_correct_answers else " "}]'
        question_markup += f'{markup_question_choice_7_prefix} {markup_question_choice_7}\n'
        if pd.notnull(markup_question_feedback_7):
            question_markup += f'... {markup_question_feedback_7}\n'

    # Choice 8
    if pd.notnull(markup_question_choice_8):
        markup_question_choice_8_prefix = f'[{"*" if markup_question_choice_8 in question_correct_answers else " "}]'
        question_markup += f'{markup_question_choice_8_prefix} {markup_question_choice_8}\n'
        if pd.notnull(markup_question_feedback_8):
            question_markup += f'... {markup_question_feedback_8}\n'

    # Choice 9
    if pd.notnull(markup_question_choice_9):
        markup_question_choice_9_prefix = f'[{"*" if markup_question_choice_9 in question_correct_answers else " "}]'
        question_markup += f'{markup_question_choice_9_prefix} {markup_question_choice_9}\n'
        if pd.notnull(markup_question_feedback_9):
            question_markup += f'... {markup_question_feedback_9}\n'

    # Choice 10
    if pd.notnull(markup_question_choice_10):
        markup_question_choice_10_prefix = f'[{"*" if markup_question_choice_10 in question_correct_answers else " "}]'
        question_markup += f'{markup_question_choice_10_prefix} {markup_question_choice_10}\n'
        if pd.notnull(markup_question_feedback_10):
            question_markup += f'... {markup_question_feedback_10}\n'

    return question_markup