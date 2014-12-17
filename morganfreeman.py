import random as r

#Morgan Freeman.... because why not?


def hub():
    input("WELCOME TO THE MORGAN FREEMAN QUIZ!(Press Enter")
    q1()

def q1():
    swoog=input("What is Morgan Freemans first name? >>>").strip().title()
    if swoog=="Morgan":
        print("Congrats. Yippe freeking doo.")
        q2()
    elif swoog=="Freeman":
        print("Them reading skills doe")
        q1()

    else:
        print('-_-')
        q1()
    

def q2():
    var=input("What is his last name")
    
    

questions=[q1,q2]

def quest():
    question=r.choice(questions)
    print(question)


quest()










