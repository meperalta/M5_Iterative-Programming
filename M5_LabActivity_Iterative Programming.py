#Maria Eden Peralta
#February 19, 2022

#Problem 1

for i in range(0,100):
    print("Hello World")

#Problem 2
#a
numbers = list((0,12,10,32,3,66,17,42,99,20)) 
for i in range(0,10):
    print(numbers[i])
    
#b
numbers = list((0,12,10,32,3,66,17,42,99,20)) # note the double round-brackets
for i in range(0,10):
    numberssquare= numbers[i] *numbers[i] 
    print(numbers[i] ," " , numberssquare )


#Problem 3
    
import turtle
wn = turtle.Screen()
eden = turtle.Turtle()
wn.bgcolor("lightgreen")

for aColor in ["yellow", "red", "purple", "blue"]:      
    eden.color(aColor)
    eden.forward(50)
    eden.left(90)
    
eden = turtle.Turtle()  

wn.exitonclick()

#Problem 4

for i in range(3):
    print(list(range(0, 50, 3)))

for i in range(5):
    print(list(range(0, 50, 5)))
    
#Problem 5

import turtle
wn = turtle.Screen()             
wn.bgcolor("lightblue")


eden = turtle.Turtle()           
eden.color("hotpink")
eden.pensize(6)

eden = turtle.Turtle()           

eden.forward(80)                 
eden.left(120)
eden.forward(80)
eden.left(120)
eden.forward(80)
eden.left(120)                   

eden.right(180)                  
eden.forward(80)                 

eden.forward(50)                 
eden.left(90)
eden.forward(50)
eden.left(90)
eden.forward(50)
eden.left(90)
eden.forward(50)
eden.left(90)

wn.exitonclick()
