import datetime
import random

from questions import Add, Multiply


class Quiz:
    questions = []
    answers = []

    def __init__(self):
        #generate 10 rand questions with numbers from 1 to 10
        question_types = (Add, Multiply)
        for _ in range(10):
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            question = random.choice(question_types)
            #add generated questions into self.questions
            self.questions.append(question(num1, num2))

    def take_quiz(self):
        #log start time
        self.start_time = datetime.datetime.now()
        #ask all questions
        for question in self.questions:
            #log if question right
            self.answers.append(self.ask(question))
        else:
            #log end time
            self.end_time = datetime.datetime.now()
        #show summary
        return self.summary()

    def ask(self, question):
        correct = False
        #log start
        question_start = datetime.datetime.now()
        #capture answer
        answer = input(question.text + ' = ')
        #check answer
        if answer == str(question.answer):
            correct = True
        #log end time
        question_end = datetime.datetime.now()
        #if answer is right,
            #send true
        #else
            #send false
        #send back elapsed time
        return correct, question_end - question_start

    def total_correct(self):
        #return total # of correct questions
        total = 0
        for answer in self.answers:
            if answer[0]:
                total += 1
        return total


    def summary(self):
        #print how many questions were right
        print("You got {} out of {} correct!".format(self.total_correct(), len(self.questions)))
        #print how long it took
        print("It took you {} seconds total".format((self.end_time - self.start_time).seconds))
Quiz().take_quiz()
