import os
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


questions = [
    Question(question_data[i]["text"], question_data[i]["answer"]) for i, _ in enumerate(question_data)
]

quiz_brain = QuizBrain(questions)
while quiz_brain.still_has_questions():
    quiz_brain.next_question()
    
print("You've completed the quiz")
print(f"Your final score was: {quiz_brain.score}/{quiz_brain.question_number}")