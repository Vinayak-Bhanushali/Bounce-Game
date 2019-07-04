from tkinter import*
import random
import time
import sys
import os

# setting up window
tk = Tk()
tk.title("Bounce")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
canvas = Canvas(tk, width=500, height=500, bd=0, highlightthickness=0, bg = "black")
canvas.pack()
tk.update()
score = 0
speed = 0.02

scoreText = canvas.create_text(450,480,text="Score: "+str(score),fill="Green",font=("TImes",10))


class Ball:
    
    def __init__(self,canvas,paddle,color):
        self.paddle = paddle
        self.canvas = canvas
        self.id = canvas.create_oval(10,10,25,25, fill = color)
        self.canvas.move(self.id,245,100)#bring to center pos
        start = [-3,-2,-1,0,1,2,3]
        random.shuffle(start)
        self.x = start[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def hit_paddle(self,pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
            return False

    def restart(self,event):
        python = sys.executable
        os.execl(python, python, * sys.argv)

    def draw(self):
        global score
        global sa
        self.canvas.move(self.id,self.x,self.y)#move ball to position x and y
        # current cords of ball in array [x1,y1,x2,y2]
        pos = self.canvas.coords(self.id)
        #print(pos)
        if pos[1] <= 0:
            #if y1 is in negative change y axis movement to downwards
            self.y = 3
        if pos[3] >= self.canvas_height:
            #if y2 is in positive change y axis movement to upwards
            self.hit_bottom = True
            canvas.create_text(245,100,text="Game Over",fill="Red",font=("TImes",30))
            canvas.create_text(245,300,text="Press Enter To Restart",fill="White",font=("TImes",15))
            self.canvas.bind_all('<KeyPress-Return>',self.restart)
        if pos[0] <= 0:
            #if x1 is in negative change x axis movement to right
            self.x = 3
        if pos[2] >= self.canvas_width:
            #if x2 is in positive change x axis movement to left
            self.x = -3
        if self.hit_paddle(pos) == True:
            self.y = -3
            score = score + 1


class Paddle:
    
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,100,10, fill = color)
        self.canvas.move(self.id,200,400)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>',self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>',self.turn_right)        

    def draw(self):
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            #if x1 is in negative stop paddle
            self.x = 0
        if pos[2] >= self.canvas_width:
            #if x2 is in positive stop paddle
            self.x = 0
        
    def turn_left(self,event):
        self.x = -5
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            #if x1 is in negative stop paddle
            self.x = 0
        self.canvas.move(self.id,self.x,0)
    def turn_right(self,event):
        self.x = 5
        pos = self.canvas.coords(self.id)
        if pos[2] >= self.canvas_width:
            #if x2 is in positive stop paddle
            self.x = 0
        self.canvas.move(self.id,self.x,0)
        

paddle = Paddle(canvas,"blue")
ball = Ball(canvas,paddle,"orange")

while 1:
    if ball.hit_bottom == False:
        ball.draw()
        paddle.draw()
    tk.update_idletasks()
    tk.update()
    canvas.itemconfigure(scoreText,text = "Score: "+str(score))
    time.sleep(speed)
    


