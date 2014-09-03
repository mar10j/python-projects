import random


print("Your fate lies in this ball.")
print("Type your Question below.")

def ask():
    question = input(">").strip().lower()
    print(question)
    answers = ['yes','no','maybe']
    answer = random.choice(answers)
    print(answer)
while True: ask()
