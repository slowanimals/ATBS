#chapter 10 project
'''
Here is what the program does:

Creates 35 different quizzes
Creates 50 multiple-choice questions for each quiz, in random order
Provides the correct answer and three random wrong answers for each question, in random order
Writes the quizzes to 35 text files
Writes the answer keys to 35 text files
This means the code will need to do the following:

Store the states and their capitals in a dictionary.
Call open(), write(), and close() for the quiz and answer key text files.
Use random.shuffle() to randomize the order of the questions and multiple-choice options.
'''
import shelve
from pathlib import Path
import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona':
'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado':
'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida':
'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines',
'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge',
'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston',
'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln',
'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia':'Charleston', 
'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# Generate 35 quiz files
for quiz_num in range(35):
    quiz_file = open(f'capitalsquiz{quiz_num + 1}.txt', 'w', encoding = 'UTF-8')
    answer_file = open(f'capitalsquiz_answers{quiz_num + 1}', 'w', encoding = 'UTF-8')

    #headers
    quiz_file.write('Name:\nDate:\nPeriod:\n\n')
    quiz_file.write((' ' * 20) + f'Capitals Quiz (Form {quiz_num + 1})')
    quiz_file.write('\n\n')

    #shuffle order
    states = list(capitals.keys())
    random.shuffle(states)

    #Loop through all 50 states, making a question for each.
    for i in states:
        correct_answer = capitals[i]
        wrong_answers = list(capitals.values())
        del wrong_answers[wrong_answers.index(correct_answer)]
        wrong_answers = random.sample(wrong_answers, 3)
        choices = wrong_answers + [correct_answer]
        random.shuffle(choices)

    for i in range(50):
        quiz_file.write(f'Question {i + 1}. What is the capital of {states[i]}?\n')
        for i in range(4):
            quiz_file.write(f"'{'ABCD'[i]}. {choices[i]}\n")
        quiz_file.write('\n')
        answer_file.write(f"{i + 1}. {'ABCD'[choices.index(correct_answer)]}")
    
    quiz_file.close()
    answer_file.close()

