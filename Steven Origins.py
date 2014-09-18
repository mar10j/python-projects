input("WELCOME TO THE ADVENTURES OF STEVEN!     JACK MARTIN EDITION")
name = input("What is your name? >").strip().title()

if name == "Steven":
    print("Correct!")

if name != "Steven":
    print("No your name is steven.")

input("Now steven, this is your story. Okay? Good.")
input("One day you were walking around when you see a short Curly haired boy walking down the street. Being the evil creature that you are, You decide to jump inside this poor boys hair.")
di = input("As you examine the area, You realize that they hair is like a maze. Steven decides to go left, NOT RIGHT. >").strip().lower()
if di == ("left"):
    jackson = input("Good! Glad to see you are a rule follower, Steven. Now you see a evil Micheal Jackson! Will you attack or Flee?").strip().lower()
    if jackson == ("attack"):
        print("Violence is not the answer Steven! No!")
