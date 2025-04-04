import json

x = input("What mode, Teacher, Student, or Exit?")

class Flashcards:
    def __init__(self, phrase, answer):
        self.phrase= phrase
        self.answer= answer

    def flashcards(self):
        return f"{self.phrase}:{self.answer}"
    
    def to_dict(self):
        return{"question": self.phrase, "answer": self.answer}



while x != "Exit":
    if x == "Teacher":       
        class Teacher:
            def __init__(self, question, answer):
                self.question= question
                self.answer= answer


        x = Flashcards(input("Give me a word: "), input("Give me an answer: "))

        try:
            with open("flashcards.json", "r") as file:
                flashcard_data = json.load(file)
        except FileNotFoundError:
            flashcard_data = []

        flashcard_data.append(x.to_dict())

        with open("flashcards.json", "w") as file:
            json.dump(flashcard_data, file, indent=4)

        x = input("What mode, Teacher, Student, or Exit?")
    
"""     elif x == "Student":
        class Student:
            def __init__(self, tally):
 """