from question_model import Question
from data import question_data

question_bank = []

for q in question_data:
    new_question = Question(q["text"], q["answer"])
    question_bank.append(new_question)

print(question_bank)



