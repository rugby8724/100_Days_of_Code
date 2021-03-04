from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []


for question in question_data:
    new_ques = Question(question['question'], question['correct_answer'])
    question_bank.append(new_ques)


quiz = QuizBrain(question_bank)
quiz.next_question()