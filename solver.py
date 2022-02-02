from random import randint
import re
import copy

class Player:

    def __init__(self,maze):
        self.maze = maze

        for l in range(0,len(maze)):
            if "O" in maze[l]:
                for c in range(0 , len(maze[l])):
                    if maze[l][c] == "O":
                        self.pos = (c+1 , l+ 1)
                        self.x = self.pos[0]
                        self.y = self.pos[1]
            if "E" in maze[l]:
                    for c in range(0 , len(maze[l])):
                        if maze[l][c] == "E":
                            self.target = (c+1 , l + 1)
        self.start = self.pos
        
    
    def get_pos_folan(self,x , y):
        return self.maze[y-1][x-1]
    
    def number_of_spaces_around(self):
        res = 0
        x , y = self.pos[0] , self.pos[1]
        for i in [1 , -1]:
            for j in [1 , -1]:
                if self.get_pos_folan(x-i , y-j) == " ":
                    res += 1
        return res

    def move_up(self):
        self.maze[(self.y-1)-1][self.x-1]="O"
        self.maze[self.y-1][self.x-1]="."
        self.y = self.y-1
        self.pos = (self.x , self.y)


    def move_down(self):
        self.maze[self.y][self.x-1]="O"
        self.maze[self.y-1][self.x-1]="."
        self.y = self.y+1
        self.pos = (self.x , self.y)


    def move_right(self):
        self.maze[self.y-1][self.x]="O"
        self.maze[self.y-1][self.x-1]="."
        self.x = self.x+1
        self.pos = (self.x , self.y)

    def move_left(self):
        self.maze[self.y-1][self.x-1]="O"
        self.maze[self.y-1][self.x-1]="."
        self.x = self.x-1
        self.pos = (self.x , self.y)

    def overview(self):
        for line in self.maze:
            res = ""
            for c in line:
                res += c
            print(res)
        print("-"*100)

    def has_won(self):
        if self.pos[0] == self.target[0] and self.pos[1] == self.target[1]:
            x , y = self.start[0] , self.start[1]
            self.maze[y-1][x-1] = "S"
            self.maze[self.y-1][self.x-1]="E"

            return True
        else:
            return False


valid = input()
if valid != "go":
    print(" ok :|")
else:
    with open("copy here.txt" , "r") as fl:
        maze = fl.readlines()
    new_maze = []
    i = 1
    for line in maze:
        if i == 23:
            new_maze.append(list(re.sub("â–ˆ" , "=" , line)[:-1]+"="))
        else:
            new_maze.append(list(re.sub("â–ˆ" , "=" , line)[:-1]))
        i+=1
    maze = new_maze.copy()

    
    asly = copy.deepcopy(maze)
    solves = []
    for i in range(20):  #in adad ro harchi balatar bedid javab behtary migirid. amm be fekr salamaty computer khod ham bashid

        main = Player(maze)
        while main.has_won() == False:
            if main.number_of_spaces_around() == 1:
                main.pos == main.start
            a=randint(1,4)
            if a == 1 and main.get_pos_folan(main.x , main.y-1)   in " .E":
                main.move_up()
            elif a == 2 and main.get_pos_folan(main.x , main.y+1) in " .E":
                main.move_down()
            elif a == 3 and main.get_pos_folan(main.x+1 , main.y) in " .E":
                main.move_right()
            elif a == 4 and main.get_pos_folan(main.x-1 , main.y) in " .E":
                main.move_left()
        solves.append(main)
        maze = copy.deepcopy(asly)
dots = []
for obj in solves:
    res = 0
    for line in obj.maze:
        for c in line:
            if c== ".":
                res += 1
    dots.append(res)

minim = dots[0]

for i in range(0 , len(dots)):
    if dots[i] < minim:
        minim = dots[i]
        index = i
solves[index].overview()
