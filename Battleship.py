class ship():
    size = None
    def __init__(self):
            self.location

class Carrier(ship):
    size = 5

class Battleship(ship):
    size = 4

class Submarine(ship):
    size = 3

class Destroyer(ship):
    size = 3

class PatrolBoat(ship):
    size = 2


    
#-------------------------------------------------------------


print ("Welcome to the Battling of the Ships.")
#TODO  add super sweg art XD
#TODO ask the game for AI difficulty
#TODO print grid

w = '~ '
row = [
    ['A',w,w,w,w,w,w,w,w,w,w],
    ['B',w,w,w,w,w,w,w,w,w,w],
    ['C',w,w,w,w,w,w,w,w,w,w],
    ['D',w,w,w,w,w,w,w,w,w,w],
    ['E',w,w,w,w,w,w,w,w,w,w],
    ['F',w,w,w,w,w,w,w,w,w,w],
    ['G',w,w,w,w,w,w,w,w,w,w],
    ['H',w,w,w,w,w,w,w,w,w,w],
    ['I',w,w,w,w,w,w,w,w,w,w],
    ['J',w,w,w,w,w,w,w,w,w,w],
    ['K',w,w,w,w,w,w,w,w,w,w],
    ['L',w,w,w,w,w,w,w,w,w,w],
]



for


def battlesharpu():
    start_row = input("Enter start row for carrier >").strip().lower()
    start_col = input("Enter start col for carrier >").strip().lower()
    di = input("Enter the direction  for carrier [n,s,e,w] >").strip().lower()
    if di == "n":
        input("DO STUFF HERE")
    elif di == "s":
        input("DO STUFF HERE")
    elif di == "e":
        input("DO STUFF HERE")
    elif di == "w":
        input("DO STUFF HERE")
    else:
        input("I do not understand")
        battlesharpu()
    
