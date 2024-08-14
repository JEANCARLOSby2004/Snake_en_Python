import turtle
import time
import random

posponer = 0.1 #variable posponer

puntaje = 0
puntajemasalto = 0

ventana = turtle.Screen() 
ventana.title("jueguito")
ventana.bgcolor("black")
ventana.setup(width = 600, height = 600)
ventana.tracer(0)



#comando de cabeza

cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.color("white")
cabeza.shape("square")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = "stop"

#comida de serpiente

comida = turtle.Turtle()
comida.speed(0)
comida.color("red")
comida.shape("circle")
comida.penup()
comida.goto(0,100)

#cuerpo en lista
segmentos = []

#texto
texto=turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write("Puntos: 0 	puntucion mas alta: 0", align = "center", font =("courier",18,"normal"))

#funcion de direccion de cabeza
def arriba():
	cabeza.direction = "up"
def abajo():
	cabeza.direction = "down"
def izquierda():
	cabeza.direction = "left"
def derecha():
	cabeza.direction = "right"


#funcon de mivimiento
def mov():
 	if cabeza.direction == "up":
 		y = cabeza.ycor()
 		cabeza.sety(y + 20)

 	if cabeza.direction == "down":
 		y = cabeza.ycor()
 		cabeza.sety(y - 20)

 	if cabeza.direction == "left":
 		x = cabeza.xcor()
 		cabeza.setx(x - 20)

 	if cabeza.direction == "right":
 		x = cabeza.xcor()
 		cabeza.setx(x + 20)

#funcion de teclado
ventana.listen()
ventana.onkey(arriba, "Up")
ventana.onkey(abajo, "Down")
ventana.onkey(izquierda, "Left")
ventana.onkey(derecha, "Right")

while True:
	ventana.update()

	#choques con bordes
	if cabeza.xcor() >280 or cabeza.xcor() <-280 or cabeza.ycor() >280 or cabeza.ycor() < -280:
		time.sleep(1)
		cabeza.goto(0,0)
		cabeza.direction = "stop"

		#esconder segmentos
		for segmento in segmentos:
			segmento.goto(1000,1000)

		#limpiar lista de segmentos
		segmentos.clear()

		#resetear marador
		puntaje = 0
		texto.clear()
		texto.write("Puntos: {}	puntucion mas alta: {}".format(puntaje, puntajemasalto), 
			align = "center", font =("courier",18,"normal"))

	#choque con comida
	if cabeza.distance(comida) < 20:
		x = random.randint(-280,280)
		y = random.randint(-280,280)
		comida.goto(x,y)

		nuevo_segmento = turtle.Turtle()
		nuevo_segmento.speed(0)
		nuevo_segmento.color("grey")
		nuevo_segmento.shape("square")
		nuevo_segmento.penup()
		segmentos.append(nuevo_segmento)

		#aumentar marcador
		puntaje += 10
		if puntaje > puntajemasalto:
			puntajemasalto = puntaje

		texto.clear()
		texto.write("Puntos: {}       puntucion mas alta: {}".format(puntaje, puntajemasalto), 
			align = "center", font =("courier",18,"normal"))

	#mover el cuerpo
	totalseg = len(segmentos)
	for index in range(totalseg -1, 0, -1):
		x = segmentos[index - 1].xcor()
		y = segmentos[index - 1].ycor()
		segmentos[index].goto(x,y)
	if totalseg > 0:
		x = cabeza.xcor()
		y = cabeza.ycor()
		segmentos[0].goto(x,y)

	mov()

	#choque con cuerpo
	for segmento in segmentos:
		if segmento.distance(cabeza) < 20:
			time.sleep(1)
			cabeza.goto(0,0)
			cabeza.direction = "stop"

			#esconder segmentos 
			for segmento in segmentos:
				segmento.goto(1000,1000)

			segmentos.clear()
			puntaje = 0
			texto.clear()
			texto.write("Puntos: {}	puntucion mas alta: {}".format(puntaje, puntajemasalto), 
			align = "center", font =("courier",18,"normal"))


	time.sleep(posponer)
 