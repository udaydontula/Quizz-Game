# from main import question_bank

class QuizBrain:

    def __init__(self, q_list):
        self.question_no = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        if self.question_no < len(self.question_list):
            return True
        else:
            return Falsed



    def next_question(self):

        current_question = self.question_list[self.question_no]
        self.question_no += 1
        x = input(f"Q.no {self.question_no} : {current_question.text} (True/False):")
        self.check_answer(x, current_question.answer)

    def check_answer(self, x, correct_answer):
        if x.lower() == correct_answer.lower():
            self.score += 1
            print(f"Your Score: {self.score}/{self.question_no}")
            print(f"The correct answer is {correct_answer}")
        else:
            print("Wrong answer")
            print(f"Your Score: {self.score}/{self.question_no}")
            print(f"The correct answer is {correct_answer}")
