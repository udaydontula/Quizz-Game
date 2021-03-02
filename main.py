from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    text = question["text"]
    answer = question["answer"]
    q_bank = Question(text, answer)
    question_bank.append(q_bank)

quiz = QuizBrain(question_bank)
# quiz.next_question()

while quiz.still_has_question():
    quiz.next_question()
