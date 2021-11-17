from chap_6.question_model import Question
from chap_6.quiz_brain import QuizBrain
from chap_6.data import question_data

question_bank = []
for data in question_data:
    new_q = Question(data.get("text"), data.get("answer"))
    question_text = data.get("text")
    question_answer = data.get("answer")
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()