                                # QUIZ PROJECT

import random

capital = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis'}

for num in range(20):
    quizfile = open(f'capitalquiz {num + 1}.txt', 'w')
    answerfile = open(f'capitalanswers{num + 1}.txt', 'w')
    quizfile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizfile.write((' ' * 5) + f'State Capitals Quiz (Form{num + 1})')
    quizfile.write('\n\n')

    state = list(capital.keys())
    random.shuffle(state)

    correctanswer = capital[state[num]]
    wronganswers = list(capital.values())
    del wronganswers[wronganswers.index(correctanswer)]
    wronganswers = random.sample(wronganswers, 3)
    answerOption = wronganswers + [correctanswer]
    random.shuffle(answerOption)

    quizfile.write(f'{num + 1}. What is the capital of{state[num]}?\n')
for i in range(4):
    quizfile.write(f"    {'ABCD'[i]}. { answerOption[i]}\n")
    quizfile.write('\n')

    answerfile.write(f"{num + 1}.{'ABCD'[answerOption.index(correctanswer)]}")
quizfile.close()
answerfile.close()

'''
this is a program which ask MCQ questions with options

'''










