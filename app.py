import json
x = input("Teacher or Student or Exit?: ")

while x != "Exit":
    if x == "Teacher":
        class Teacher:
            def __init__(self, key, value):
                self.key= key
                self.value= value

            def flashcards(self):
                return f"{self.key}:{self.value}"
            
        words = Teacher(input("Give me a word: "), input("Give me an answer: "))
        flashcards_data = [word.to_dict() for word in words]
        try:
            with open("flashcards.json", "r") as file:
                words = json.load(file)
        except FileNotFoundError:
            flashcards_data = []