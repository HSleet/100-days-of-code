from question_model import Question

class QuizBrain:
    
    def __init__(self, question_list: list[Question]):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
    
    def next_question(self):
        current_question = self.question_list[self.question_number]
        answer = input(f"Q.{self.question_number + 1}: {current_question.text} (True/False): ").capitalize()
        self.question_number += 1
        if answer  == current_question.answer:
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {current_question.answer}.")
        print(f"Your current score: {self.score}/{self.question_number}")
        print("\n\n")
        
    
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
