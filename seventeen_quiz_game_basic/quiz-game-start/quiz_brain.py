

class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.correct_number = 0
        self.question_list = questions_list

    def still_has_questions(self,):
        return self.question_number + 1 < len(self.question_list)

    def next_question(self,):
        while self.still_has_questions():
            current_quest = self.question_list[self.question_number]
            self.question_number += 1
            user_answer = input(f'Q.{self.question_number}: {current_quest.text} (True/False) ')
            self.check_answer(user_answer, current_quest.answer)
        self.quiz_complete()

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print('You got it right!')
            self.correct_number += 1
        else:
            print('Sorry that is not correct')
        print(f'The correct answer was: {correct_answer}')
        print(f'Your current score is: {self.correct_number}/{self.question_number}')
        print('\n')

    def quiz_complete(self):
        print('You completed the quiz')
        print(f'Here is your final score {self.correct_number}/{self.question_number}')








