#importacion de carpetas
import time;
from random import randint;
import turtle;

#declaracion e inicializacion de variables necesarias
acont = int();
bcont = int();
a = int();
b = int();

acont = 0;
bcont = 0;
a = 0;
b = 0;

#dibujo de lineas
xpos = -200
ypos = 200

line = turtle.Turtle();
line.penup();
line.goto(xpos, ypos);
line.right(90);
line.speed(100);


while(xpos < 330):
    line.pendown();
    line.forward(400);
    line.penup();
    xpos = xpos+50;
    line.goto(xpos, ypos);

xpos = 400;  
line.goto(xpos, ypos);

#linea de llegada
contline = 0
while (contline < 10):
    
    line.pendown()
    line.forward(20)
    line.penup()
    line.forward(20)
    contline = contline + 1
    line.write("llegada")


#creacion de tortugas y posicion inicial
tred = turtle.Turtle();
tred.color("red");
tred.shape("turtle");

tred.penup();
tred.goto(-300, 50);
tred.pendown();

tblue = turtle.Turtle();
tblue.color("blue");
tblue.shape("turtle");

tblue.penup();
tblue.goto(-300, -50);
tblue.pendown();

while (True):
    
    a = randint(10, 40);
    b = randint(10, 40);
    

    tred.forward(a);
    tblue.forward(b);
    time.sleep(0.1);
    acont = acont + a;
    bcont = bcont + b;

    if ( acont >= xpos+300 ):
        break;
    elif ( bcont >= xpos+300 ):
        break;

#mensajes de victoria
if (acont >= xpos+300 and bcont >= xpos+300):
    if (acont > bcont):
        turtle.write("Red turtle wins");
    elif (acont < bcont):
        turtle.write("Blue turtle wins");
    else:
        turtle.write("Its a tie!");
        
elif (acont >= xpos+300 and bcont < xpos+300):
    turtle.write("Red turtle wins");
    
elif (acont < xpos+300 and bcont >= xpos+300):
    turtle.write("Blue turtle wins");


time.sleep(10)











    

