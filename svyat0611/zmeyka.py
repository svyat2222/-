import time
import turtle
from random import randrange

# экран для игры
screen= turtle. Screen()
#название
screen.title('Snake with turtle module')
#задний фон
screen.bgcolor('white')
#размер экрана
screen.setup(650,650)
screen.tracer(0)
#рисуем грааница
border = turtle.Turtle()
border . hideturtle()
border . penup()
border . goto(-311,311)
border . pendown()
border . goto(311,311)
border . goto(311,-311)
border . goto(-311,-311)
border . goto(-311,311)



#змейка
snake = []
for i in range(3):
	snake_segment = turtle.Turtle()
	#"форма" змейки
	snake_segment.shape('square')
	snake_segment.penup()
	if i > 0:
		snake_segment.color('grey')
	#дабавляем змейку в список
	snake.append(snake_segment)

#дэлаем еду
food = turtle.Turtle()
food.shape('circle')
food.penup()
#рандомная еда
food.goto(randrange(-300, 300, 20), randrange(-300, 300, 20))


#контроль змейки
screen.onkeypress(lambda: snake[0].setheading(90), 'Up')
screen.onkeypress(lambda: snake[0].setheading(270), 'Down')
screen.onkeypress(lambda: snake[0].setheading(180), 'Left')
screen.onkeypress(lambda: snake[0].setheading(0), 'Right')
#слушаэт экран
screen.listen()
#----------------------основной цикл програмы---------------------------
while True:
	 
	#
	if snake[0].distance(food) < 10:
		food.goto(randrange(-300, 300, 20), randrange(-300, 300, 20))
		snake_segment = turtle.Turtle()
		snake_segment.shape('square')
		snake_segment.color('gray')
		snake_segment.penup()
		snake.append(snake_segment)
	 
	#размещаем змейку
	for i in range(len(snake)-1, 0, -1):
		x = snake[i-1].xcor()
		y = snake[i-1].ycor()
		#размещает в точке x, y
		snake[i].goto(x, y)
		
		  
	# движение головы
	snake[0].forward(20)
	#fps
	screen.update()
	
	#граници экрана
	x_cor = snake[0].xcor()
	y_cor = snake[0].ycor()
	#
	if x_cor > 300 or x_cor < -300:
		screen.bgcolor('red')
		break
	if y_cor > 300 or y_cor < -300:
		screen.bgcolor('red')
		break
	
	#обновления екрана
	time.sleep(0.15)


#Шоб не вылетало
screen.mainloop()
screen.done()
