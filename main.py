from question_model import Question
from data import question_data
from quiz_brain import QuizzBrain

question_bank = []
for question in question_data:
    new_q = Question(question['text'], question['answer'])
    question_bank.append(new_q)

quiz = QuizzBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print(f"You've completed the quiz.\nYou're final score was:  {quiz.score}/{quiz.question_number}")