class QuizBrain:

    def __init__(self, question_list):
        self.score = 0
        self.question_list = question_list
        self.question_number = 0

    def next_question(self):
        ques = self.question_list[self.question_number]
        self.question_number += 1
        choice = input(f"Q.{self.question_number}: {ques.text} (True/False): ").lower()
        self.is_correct(choice, ques.answer)
        print("\n")

    def is_correct(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right.")
        else:
            print("Oops, it was the wrong answer")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your score is: {self.score}/{self.question_number}")

    def more_questions(self):
        return len(self.question_list) > self.question_number
