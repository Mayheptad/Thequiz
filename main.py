
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for qD in question_data:
    question_bank.append(Question(qD['text'], qD['answer']))

quiz = QuizBrain(question_bank)

while quiz.still_have_question():
    quiz.next_question()

