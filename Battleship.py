class Ship():
    size = None
    def __init__(self):
            self.location

class Carrier(ship):
    size = 5

class Battleship(ship):
    size = 4

class Submarine(Ship):
    size = 3

class Destroyer(Ship):
    size = 3

class PatrolBoat(ship):
    size = 2


    
#-------------------------------------------------------------


print ("Welcome to the Battling of the Ships.")
#TODO  add super sweg art XD
#TODO ask the game for AI difficulty
#TODO print grid

grid = [[' ~' * 10] * 10]

for row in grid:
    for col in row:
        print (col)

start_row = input("Enter start row for carrier >").strip().lower()
start_col = input("Enter start col for carrier >").strip().lower()
di = input("Enter the direction  for carrier [n,s,e,w] >").strip().lower()

