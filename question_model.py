from data import question_data

class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

question_bank = []
for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))


print(question_bank[0].text)
print(question_bank[0].answer)
print(question_bank)