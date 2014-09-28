import random

print("This is a magic 8 ball.")
print("Type in your fate.")

def ask():
    qu = input(">")
    answers = ["Yes","No","Maybe"]
    answer = random.choice(answers)
    print(answer)





while True: ask()
