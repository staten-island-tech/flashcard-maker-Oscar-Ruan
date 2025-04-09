import json

x = input("What mode, Teacher, Student, or Exit?")
play = 0

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


        a = Flashcards(input("Give me a word: "), input("Give me an answer: "))

        try:
            with open("flashcards.json", "r") as file:
                flashcard_data = json.load(file)
        except FileNotFoundError:
            flashcard_data = []

        flashcard_data.append(a.to_dict())

        with open("flashcards.json", "w") as file:
            json.dump(flashcard_data, file, indent=4)

        x = input("What mode, Teacher, Student, or Exit?")
    
    elif x == "Student":
        Flashcard = open("./flashcards.json", encoding="utf8")
        data = json.load(Flashcard)
        
        y = input("continue? ")

        while y == "yes":
            for cards in data:
                print(cards["question"])
                b = input("what is the answer? ")
                if b == (cards["answer"]):
                    print("correct")
                    play = play + 1
                    y = input("continue?")
        else:
            break
