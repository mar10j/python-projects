import random


print("Your fate lies in this ball.")
print("Type your Question below.")

def ask():
    question = input(">").strip().lower()
    answers = ['Yes','No','Maybe',"Don't get cocky","Please ask again","Not likely","Of course","Ask someone else","100% Yes!","Never gonna happen","In your dreams"]
    answer = random.choice(answers)
    print(answer)
while True: ask()
