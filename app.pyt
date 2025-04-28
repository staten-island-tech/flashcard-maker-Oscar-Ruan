import json
x = input("What mode: ")
points = 0
streak = 0

class Flashcards:
    def __init__(self, question, answer):
        self.question= question
        self.answer= answer
    def to_dict(self):
        return{"question": self.question, "answer": self.answer}

if x == "Teacher":
    flash = Flashcards(input("Give me a word: "), input("Give me an answer: "))

    try:
        with open("flashcards.json", "r") as file:
            flashcard_data = json.load(file)
    except FileNotFoundError:
        flashcard_data = []

    flashcard_data.append(flash.to_dict())

    with open("flashcards.json", "w") as file:
        json.dump(flashcard_data, file, indent=4)

elif x == "Student":
    Flashcard = open("./flashcards.json", encoding="utf8")
    data = json.load(Flashcard)
    z = input("continue? ")

    while z == ("yes"):
        for i in data:
            print(i["question"])
            y = input("what is the answer?")
            if y == i["answer"]:
                print(f"The answer is {i["answer"]}")
                print("correct")
                points += 1
                streak += 1
                print(f"streak:{streak}")
                print(f"points:{points}")
                z = input("continue? ")
                if streak >= 3:
                    points += 1
            else:
                print(i["answer"])
                streak = 0
                print("wrong")
                print(f"points:{points}")
                print(f"streak:{streak}")
                z = input("continue? ")
            if z == "no":
                break
            
else:
    print("Only type Teacher or Student :p")
