from tkinter import *
import random
from sys import exit


class Snake():
    def __init__(self,canvas,body_size, body_parts, snake_color = "#00FF00", direction = "right"):

        self.coordinates = [[0,0]]

        self.canvas = canvas
        self.body_size = body_size
        self.snake_color = snake_color
        self.body_parts = body_parts
        self.squares =[self.canvas.create_rectangle(self.coordinates[0][0],self.coordinates[0][1],self.coordinates[0][0]+self.body_size,self.coordinates[0][1]+self.body_size,fill = self.snake_color, tag = "snake")]
        self.direction = direction


    def move(self,direction):

        match direction:
            case "right":
                new_coords = [self.coordinates[0][0]+self.body_size,self.coordinates[0][1]]
                self.coordinates.insert(0,new_coords)
            case "left":
                new_coords = [self.coordinates[0][0]-self.body_size,self.coordinates[0][1]]
                self.coordinates.insert(0,new_coords)
            case "up":
                new_coords = [self.coordinates[0][0],self.coordinates[0][1]-self.body_size]
                self.coordinates.insert(0,new_coords)
            case "down":
                new_coords = [self.coordinates[0][0],self.coordinates[0][1]+self.body_size]
                self.coordinates.insert(0,new_coords)
            case "_":
                return "Invalid"
            

        x = new_coords[0]
        y = new_coords[1]

        # might have to modify
        self.canvas.delete(self.squares[0])

        self.squares.pop(0)
        self.coordinates.pop(-1)   
        square = self.canvas.create_rectangle(x,y,x+self.body_size,y+self.body_size,fill = self.snake_color, tag = "snake")
        self.squares.append(square)
  
    def grow(self):
        pass

class Fruit():
    pass

class Game():
    def __init__(self, GAME_HEIGHT = 500, GAME_WIDTH  = 500,TICK_SPEED = 500, SPACE_SIZE = 50, BODY_PARTS = 3, ):
        self.window = Tk()
        self.window.title("Snek Game")
        self.window.attributes(topmost=True)
        self.window.resizable(False,False)
        self.window.geometry(f"{GAME_WIDTH+100}x{GAME_HEIGHT+100}")

        self.score = 0

        self.game_width = GAME_WIDTH
        self.game_height = GAME_HEIGHT
        self.tick_speed = TICK_SPEED
        self.direction = "right"

        self.label = Label(self.window,text = f"Score:{self.score}", font = ("montserrat",40), background="#57BD7E")
        self.label.pack(expand =True)
    
        self.canvas = Canvas(self.window,height=GAME_HEIGHT,width=GAME_WIDTH, bg = "black")
        self.canvas.pack()
        self.snake=Snake(self.canvas,SPACE_SIZE,BODY_PARTS)


    def next_tick(self):
        self.snake.move(self.direction)
        if self.check_collisions():
            self.label.config(text="You're dead!'")
        else:
            self.label.config(text="You're alive!")
        self.window.after(self.tick_speed,self.next_tick)
        print(self.snake.coordinates)

    def change_direction(self,event):
        match event.keycode:
            case 114:
                self.direction = "right"
            case 113:
                self.direction = "left"
            case 111:
                self.direction = "up"
            case 116:
                self.direction = "down"
        # print(self.direction)

    def check_collisions(self):
        if self.snake.coordinates[0][0] <0 or self.snake.coordinates[0][0] > self.game_width-50 or self.snake.coordinates[0][1] <0 or self.snake.coordinates[0][1] > self.game_height-50:
            return True

    def run(self) -> None :
        self.window.bind("<Up>", self.change_direction)
        self.window.bind("<Down>", self.change_direction)
        self.window.bind("<Left>", self.change_direction)
        self.window.bind("<Right>", self.change_direction)
        self.next_tick()
  
        self.window.mainloop()

g= Game()

print(g.snake.coordinates)
g.run()