import question4
from file_handler import download_csv_sheet


def run():
    with open('survey_results_public.csv', encoding='utf-8') as f:
        print_question_separator('4. What is the most popular IDE?')
        question4.run(f)


def print_question_separator(question_number):
    print('\nQuestion ' + str(question_number), end='\n' + 100 * '-' + '\n')


run()
# It is really bugging me that you have to define function before you call it, so I wrapped everything in run()
# Thanks to that I can order functions as they are called, so you can read code from top to bottom
