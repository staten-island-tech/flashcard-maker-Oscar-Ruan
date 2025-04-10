import json

class Flashcards:
    def __init__(self, question, answer):
        self.question= question
        self.answer= answer
    def display_info(self):
        return f"{self.question}:{self.answer}"

class Teacher:
    def __init__(self, inputting_question, inputting_answer):
        self.inputting_question= inputting_question
        self.inputting_answer= inputting_answer
Teacher = Flashcards(input("enter question: "), input("enter the answer: "))
