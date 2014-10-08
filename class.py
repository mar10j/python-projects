class Grid():

    def __init__(self,rows=10,cols=1,char='~'):
        self.cols = []
        for count in range(cols):
            self.cols.append(char)
            
        

class Player():
    pass

class ComputerPlayer(Player):
    pass

class Human(Player):
    pass

class ShellController():

    def run(self):
        print('Welcome to Connect4')

if __name__=='__main__':


    #game = ShellController()
    #game.run()
    grid = Grid(10,10,"O")
    print(grid.cols)


