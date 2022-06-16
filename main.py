from data import question_data2 as question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for i in range(len(question_data)):
    question_bank.append(Question(question_data[i]['question'], question_data[i]['correct_answer']))

quiz = QuizBrain(question_bank)
while quiz.more_questions():
    quiz.next_question()
print(f"You completed the quiz and your final score is: {quiz.score}/{len(quiz.question_list)}")
