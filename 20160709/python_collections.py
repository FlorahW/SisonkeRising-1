from tkinter import *

tk = Tk()

  

MY_CARS= {1 : 'Honda', 2 : 'Ford', 3 : 'Jeep', 4 : 'Chervolet SS', 5 : 'BMW'}

def display_cars(MY_CARS):
    for cars in MY_CARS:
        print(cars ,MY_CARS[cars]) 


canvas = Canvas (Tk(), width = 400 , height = 400)
canvas.pack()
btn = Button (canvas,text = 'Display Cars', command = display_cars(MY_CARS))
btn.pack()
