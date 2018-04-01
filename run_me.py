import question3
import question4
import question5

def run():
    with open('survey_results_public.csv', encoding='utf-8') as f:
        print_question_separator('3. What language do most developers work in?')
        question3.run(f)
        
        print_question_separator('4. What is the most popular IDE?')
        question4.run(f)

        print_question_separator('5. What framework do most developers want to work in?')
        question5.run(f)


def print_question_separator(question_number):
    print('\nQuestion ' + str(question_number), end='\n' + 100 * '-' + '\n')


run()
# It is really bugging me that you have to define function before you call it, so I wrapped everything in run()
# Thanks to that I can order functions as they are called, so you can read code from top to bottom
