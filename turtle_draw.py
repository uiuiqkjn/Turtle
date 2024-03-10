import turtle as t
import random
import time

light = t.Turtle(visible=False)
t.speed(0)


def draw_balloon(x, y):  # 气球
    t.penup()
    t.goto(x, y)
    t.pendown()

    t.colormode(255)
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    t.color(red, green, blue)

    t.begin_fill()
    t.circle(30)
    t.end_fill()
    t.right(90)
    t.forward(30)
    t.left(90)


def draw_scene():
    t.setup(width=800, height=600)
    t.bgcolor("skyblue")

    for i in range(20):
        x = random.randint(-1000, 1000)
        y = random.randint(-200, 400)
        draw_balloon(x, y)


def sun():  # 绘制太阳
    light.pensize(5)
    light.pencolor("black")
    sec = int(time.time())
    t.penup()  # 画红色点
    t.goto(-930, 610)
    t.pendown()
    t.dot(100, "red")
    for i in range(1, 19):  # 阳光效果
        light.penup()
        light.goto(-930, 610)
        light.seth(i * 20)
        light.forward(55)
        light.pendown()
        if (i + sec) % 2 == 1:
            light.forward(15)
        else:
            light.forward(7)


def person(pos_x=0, pos_y=0):  # 人
    t.penup()
    t.goto(pos_x, pos_y)
    t.pendown()

    t.dot(44, "#FFDEAD")
    t.right(90)
    t.penup()
    t.forward(25)
    t.right(15)
    t.pendown()
    t.pensize(10)
    t.forward(50)

    t.right(35)
    t.forward(50)
    t.back(50)
    t.left(90)
    t.forward(27)
    t.right(110)
    t.forward(23)

    t.penup()
    t.goto(pos_x, pos_y)
    t.seth(-90)
    t.forward(25)
    t.right(15)
    t.forward(20)
    t.right(60)
    t.pendown()
    t.forward(50)
    tep_x1, tep_y1 = t.xcor(), t.ycor()
    t.back(50)
    t.right(160)
    t.forward(30)
    t.seth(90)
    t.forward(20)

    t.penup()
    t.goto(tep_x1, tep_y1)
    t.seth(-145)
    t.pensize(6)
    t.pendown()
    t.forward(50)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(15)
    t.right(90)
    t.forward(20)
    t.left(90)
    t.forward(150)


def cloud(pos_x=0, pos_y=0, size=20):  # 绘制云
    pos = int(time.time())
    pos %= 50
    light.penup()
    light.goto(pos * 8 + pos_x, pos_y)

    light.fillcolor("#E6E6FA")
    light.begin_fill()
    light.seth(-80)
    light.circle(size, 110)
    for i in range(1, 6):  # 绘制下半部分
        light.right(100)
        light.circle(size, 110)
    light.left(120)
    for i in range(1, 7):
        light.right(100)
        light.circle(size, 110)
    light.end_fill()


def lie():
    t.penup()
    t.goto(0, -500)
    t.pencolor('green')
    t.write("My Hometown", align='center', font=('Arial', 75, 'normal'))


# Call the function to draw the scene
draw_scene()
sun()
person(pos_x=0, pos_y=-200)
cloud(pos_x=0, pos_y=500, size=20)
lie()

t.hideturtle()
t.mainloop()
