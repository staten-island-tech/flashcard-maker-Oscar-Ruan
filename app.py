import json
x = input("Teacher or Student or Exit?: ")

class Flashcards:
    def __init__(self, phrase, answer):
        self.phrase= phrase
        self.answer= answer

        def flashcards(self):
            return f"{self.phrase}:{self.answer}"
        
        def to_dict(self):
            return{"question": self.phrase, "answer": self.answer}
        
class Teacher(Flashcards):
            



































"""         

while x != "Exit":
    if x == "Teacher":
        class Teacher:
            def __init__(self, key, value):
                self.key= key
                self.value= value

            def flashcards(self):
                return f"{self.key}:{self.value}"
            
            def to_dict(self):
                return{"key": self.key, "value": self.value}
            
        words = Teacher(input("Give me a word: "), input("Give me an answer: "))
        
        try:
            with open("flashcards.json", "r") as file:
                flashcards_data = json.load(file)
        except FileNotFoundError:
            flashcards_data = []

        flashcards_data.append(words.to_dict())
        
        with open("flashcards.json", "w") as file:
            json.dump(flashcards_data, file, indent=4)

        x = input("Teacher or Student or Exit?: ")

    if x == "Student":
        class Student:
            def __init__(self):
                 """