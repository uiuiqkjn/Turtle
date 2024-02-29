import turtle as t
import random
import time

# 创建画布
t.setup(width=800, height=600)
t.bgcolor("skyblue")  # 设置背景颜色为天蓝色


# 控制速度
t.speed(0)


# 绘制气球
for i in range(20):
    # 随机位置
    x = random.randint(-1000, 1000)
    y = random.randint(250, 600)
    t.penup()
    t.goto(x, y)
    t.pendown()

    # 随机色彩
    t.colormode(255)
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    t.color(red, green, blue)

    # 绘制气球
    t.begin_fill()
    t.circle(30)
    t.end_fill()
    t.right(90)
    t.forward(30)
    t.left(90)


# 绘制草地
t.penup()
t.goto(-1000, -300)
t.pendown()
t.fd(-250)
t.pensize(15)
t.pencolor("green")
t.seth(-40)
for i in range(24):
    t.circle(40, 80)
    t.circle(-40, 80)
t.circle(40, 80 / 2)
t.fd(40)
t.circle(16, 180)
t.fd(40 * 2 / 3)


# 绘制太阳花
t.pensize(2)
t.penup()
t.goto(-400, -100)
t.pendown()
t.pencolor("red")
t.fillcolor("yellow")
t.begin_fill()
for i in range(50):
      t.forward(200)
      t.left(170)
t.end_fill()
t.showturtle()
t.penup()
t.goto(-500, -110)
t.pendown()

t.penup()
t.setheading(270)
t.pendown()


# 绘制房屋
# 绘制房屋主体
t.penup()
t.goto(400, 0)
t.pendown()
t.color('blue')
t.begin_fill()
for i in range(4):
    t.forward(400)
    t.right(90)
t.end_fill()
# 绘制屋顶
t.color('red')
t.penup()
t.goto(400, 0)
t.pendown()
t.begin_fill()
t.goto(200, 150)
t.goto(0, 0)
t.goto(400, 0)
t.end_fill()
# 绘制门
t.color('brown')
t.penup()
t.goto(220, -400)
t.pendown()
t.begin_fill()
t.left(180)
t.forward(150)
t.right(90)
t.forward(80)
t.right(90)
t.forward(150)
t.right(90)
t.forward(80)
t.end_fill()
t.color('yellow')
t.penup()
t.goto(250, -300)
t.pendown()
t.begin_fill()
t.circle(5)
t.end_fill()
# 绘制窗户
t.penup()
t.goto(40, -200)
t.pendown()
t.right(90)
t.begin_fill()
for i in range(4):
    t.forward(100)
    t.right(90)
t.end_fill()
t.color('white')
t.penup()
t.goto(40, -150)
t.pendown()
t.pensize(8)
t.right(90)
t.forward(100)
t.penup()
t.goto(90, -100)
t.pendown()
t.right(90)
t.forward(100)


# 隐藏箭头
t.hideturtle()


# 保持窗口打开
t.mainloop()
