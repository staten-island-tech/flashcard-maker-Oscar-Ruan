import json
x = input("What mode: ")

class Flashcards:
    def __init__(self, question, answer):
        self.question= question
        self.answer= answer
    def to_dict(self):
        return{"question": self.question, "answer": self.answer}

while x == "Teacher":
    flash = Flashcards(input("Give me a word: "), input("Give me an answer: "))
    x = input("What mode: ")

try:
    with open("flashcards.json", "r") as file:
        flashcard_data = json.load(file)
except FileNotFoundError:
    flashcard_data = []

flashcard_data.append(flash.to_dict())

with open("flashcards.json", "w") as file:
    json.dump(flashcard_data, file, indent=4)

while x =="Student":
    Flashcard = open("./flashcards.json", encoding="utf8")
    data = json.load(Flashcard)

    print(flash["question"])
    b = input("what is the answer? ")
    if b == (flash["answer"]):
        print("correct")
        play = play + 1
        x = input("What mode: ")
