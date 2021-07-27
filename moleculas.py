
'''COMANDOS



n/m= zoom +1/-1


w, s, a, d = desplaza, x, y 

flechas = modifica velocidad

z/x = encoge/agranda tamano marco rebote  
e/r = desactiva/activa rebote

'''

from random import randint

import numpy as np 
import pygame
import time



import os
#from os import listdir
#from os.path import isfile, isdir


pygame.init()
###########
#CONSTANTES


# Define some colors

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE =  (0, 0, 255)

ancho=1200
alto= 700

global size
size = [ancho, alto]

centro=[ancho/2,alto/2]

global screen
screen = pygame.display.set_mode(size)


pygame.mouse.set_visible(False)





# INICIA LISTAS DE OBJETOS


Lb=[]


zoom=1
global marco
marco=10/10

corrX=0
corrY=0
activarebote=False
TEXTOREBOTE=f'rebote {activarebote}, r= True, e= False'
Croc=0.99  #Coef roce al movimiento
Cbro=0.01   # Coef movimiento Browniano

factorvelocidad=10000000


#ATOMOS
oxigeno=10
cargaoxigeno=-2
masaoxigeno=16

hidrogeno=30
cargahidrogeno=1
masahidrogeno=2

carbono=4
cargacarbono=-4
masacarbono=12

nitrogeno=2
carganitrogeno=3
masanitrogeno=14

soles=0




#### CLASES Y FUNCIONES

class BOLA():
	def __init__(self, x, y, xvel, yvel, masa, carga, color):
	 
		self.x = x
		self.y = y	
		
		self.xvel= xvel
		self.yvel= yvel
		
		self.masa=masa
		self.carga=carga
		
		self.color=color
		
		
		self.tamano=self.masa
		


# BOLA (x, y, xvel, yvel, masa, carga, color)
for i in range(soles):
	Sol = BOLA(ancho*5/10,alto*5/10, 0, 0, 100, 1, YELLOW)
	Lb.append(Sol)

for i in range(oxigeno):
	Xinicial=randint(centro[0]-ancho*marco,centro[0]+ancho*marco)
	Yinicial=randint(centro[1]-alto*marco,centro[1]+alto*marco)
	Xvelinicial=randint(-10,10)/factorvelocidad
	Yvelinicial=randint(-10,10)/factorvelocidad

	Lb.append(BOLA(Xinicial,Yinicial,Xvelinicial,Yvelinicial, masaoxigeno, cargaoxigeno, BLUE))
#Lb.append(Planeta)

# BOLA (x, y, xvel, yvel, masa, carga, color)
#hidrogeno

for i in range(hidrogeno):
	Xinicial=randint(centro[0]-ancho*marco,centro[0]+ancho*marco)
	Yinicial=randint(centro[1]-alto*marco,centro[1]+alto*marco)
	Xvelinicial=randint(-10,10)/factorvelocidad
	Yvelinicial=randint(-10,10)/factorvelocidad

	Lb.append(BOLA(Xinicial,Yinicial,Xvelinicial,Yvelinicial, masahidrogeno, cargahidrogeno,  WHITE))
	

for i in range(carbono):
	Xinicial=randint(centro[0]-ancho*marco,centro[0]+ancho*marco)
	Yinicial=randint(centro[1]-alto*marco,centro[1]+alto*marco)
	Xvelinicial=randint(-10,10)/factorvelocidad
	Yvelinicial=randint(-10,10)/factorvelocidad

	Lb.append(BOLA(Xinicial,Yinicial,Xvelinicial,Yvelinicial, masacarbono, cargacarbono,  GREEN))
	

for i in range(nitrogeno):
	Xinicial=randint(centro[0]-ancho*marco,centro[0]+ancho*marco)
	Yinicial=randint(centro[1]-alto*marco,centro[1]+alto*marco)
	Xvelinicial=randint(-10,10)/factorvelocidad
	Yvelinicial=randint(-10,10)/factorvelocidad

	Lb.append(BOLA(Xinicial,Yinicial,Xvelinicial,Yvelinicial, masanitrogeno, carganitrogeno,  YELLOW))
		



def PAUSA():
	#global TOPISIMOtext 
	global fuente
	#global posicion
	pygame.mixer.pause()
	while True:
		
		texto='PAUSA, presion O para continuar'
		fuente = pygame.font.Font(None, 30)	
		mensaje = fuente.render(texto, 1, RED)
		screen.blit(mensaje, (ancho*3/10, alto*2/10))
	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
	
		keys = pygame.key.get_pressed()
		if keys[pygame.K_o]:
			pygame.mixer.unpause()
			break
			#global k
			#k+=1
			#if k%2==1:
				#CARTEL('A JUGAR!!')
				#pygame.mixer.unpause()
				#break
				
		pygame.display.flip()		


def CARTEL(texto, posicion, tamano, color):
	fuente = pygame.font.Font(None, tamano)	
	mensaje = fuente.render(texto, 1, color)
	screen.blit(mensaje, posicion)


# def AJUSTECENTROMASA(Lb):
# 	for i in range(len(Lb)):
# 		CMvelx=


def DISTANCIA(Lb,i,j):
	r= np.sqrt((Lb[i].x-Lb[j].x)**2+((Lb[i].y-Lb[j].y)**2))
	return r
	
	
	
	
def Felectrica(Lb,i,j):
	if i!=j:
		r=DISTANCIA(Lb,i,j)
		if r<100:
			r=100
	
	
		fuerza=-10*(10/r**2-10/r)*Lb[i].carga*Lb[j].carga
		#-1/r*10
	
		distX=Lb[i].x-Lb[j].x
		Fx=fuerza*distX/r
	
		distY=Lb[i].y-Lb[j].y
		Fy=fuerza*distY/r
	
		vectorfuerza=[Fx,Fy]
	
	else:
		vectorfuerza=[0,0]
	
	return vectorfuerza

# fuerza total sobre bola i
def Ftotal(Lb,i):
	
	Xfuerzasobre_i=0.0
	Yfuerzasobre_i=0.0
	for j in range(len(Lb)):
		Xfuerzasobre_i+=Felectrica(Lb, i, j)[0]
		Yfuerzasobre_i+=Felectrica(Lb, i, j)[1]
	return [Xfuerzasobre_i, Yfuerzasobre_i]



def suma(vector1,vector2):
    n=len(vector1)
    m=len(vector2)
    if n==m:
        
        x=[]
        for i in range(n):
            x.append(vector1[i]+vector2[i])
  
        return x
    else:
        print('distinto tamano')


def main():

	size = [ancho, alto]
	screen = pygame.display.set_mode(size)
	pygame.display.set_caption("SISTEMA DE MOLECULAS")
	clock = pygame.time.Clock()
	
	global TIEMPO
	TIEMPO=0
	
	global zoom
	global corrX
	global corrY
	global activarebote
	global TEXTOREBOTE
	global Croc
	global Cbro

	global marco


# ::::::::::::::::::::::LOOP PRINCIPAL _____________________________________	
	
	while True:
			
		global Mx
		global My
		
		TIEMPO+=1
		Mx=pygame.mouse.get_pos()[0]
		My=pygame.mouse.get_pos()[1]
		Mpress= pygame.mouse.get_pressed()
		#EVENTOS TECLAS__________________________________
		keys = pygame.key.get_pressed()
		#print (Mx, My,Mpress)
	
	### DIBUJOS ----------
		
		screen.fill(BLACK)
		pygame.draw.circle(screen, RED, [Mx,My], 5, 0)
		#BORDE=pygame.draw.rect (screen, WHITE,[centro[0]-ancho*marco,centro[1]-alto*marco,2*ancho*marco,2*alto*marco], 1)
		#print (centro)
		
		#pygame.draw.rect (screen, WHITE,[100,100,100,100], 1)

		#BORDE=pygame.draw.rect (screen, WHITE,[centro[0]-ancho*marco,centro[1]+alto*marco,centro[0]-ancho*marco,centro[1]+alto*marco], 1)
		#BORDE=pygame.draw.rect (screen, WHITE,[360, 150, 600, 249], 1)
		
				
			
		#INTEGRA VELOCIDAD DESDE FUERZA/MASA
		for i in range(len(Lb)):
			Lb[i].xvel+= Ftotal(Lb,i)[0]/Lb[i].masa
			Lb[i].yvel+= Ftotal(Lb,i)[1]/Lb[i].masa
		
		
		
		# INTEGRACION DISTANCIA
		for i in range(len(Lb)):
			Lb[i].x+=Lb[i].xvel
			Lb[i].y+=Lb[i].yvel
	
	
		#CORRIGE VELOCIDAD 
		if keys[pygame.K_UP]:
			for i in range(len(Lb)):
				Lb[i].yvel+= -0.01
		if keys[pygame.K_DOWN]:
			for i in range(len(Lb)):
				Lb[i].yvel+= 0.01	
		if keys[pygame.K_LEFT]:
			for i in range(len(Lb)):
				Lb[i].xvel+= -0.01
		if keys[pygame.K_RIGHT]:
			for i in range(len(Lb)):
				Lb[i].xvel+= 0.01
	
	#VIBRACION BROWNIANA
		for i in range(len(Lb)):
			Lb[i].xvel+= randint(-10,10)*Cbro	
			Lb[i].yvel+= randint(-10,10)*Cbro	
		
	
	# ROCE
		
		for i in range(len(Lb)):
			Lb[i].xvel*=Croc
			Lb[i].yvel*=Croc
	
	#TAMANO MARCO
	
		if keys[pygame.K_x]:
			if marco>0:
				marco+=0.01
				time.sleep(0.01)
		if keys[pygame.K_z]:
			if marco>0.02:
				marco+=-0.01
				time.sleep(0.01)
	
	# MUEVE CON MOUSE

		for i in range(len(Lb)):
			if Mx-30<Lb[i].x<Mx+30 and My-30<Lb[i].y<My+30 and Mpress[0]==True:
				Lb[i].x=Mx
				Lb[i].y=My





	# REBOTA BOLAS	
		if keys[pygame.K_e]:
			activarebote=False
			#TEXTOREBOTE='rebote NO'
		if keys[pygame.K_r]:
			activarebote=True
			#TEXTOREBOTE='rebote SI'
		if activarebote:
			Creb=1
			delta=1
			for i in range(len(Lb)):
				if Lb[i].x>=centro[0]+ancho*marco:
					Lb[i].x=centro[0]+ancho*marco-delta
					Lb[i].xvel*=-Creb
				
				if Lb[i].x<=centro[0]-ancho*marco:
					Lb[i].x=centro[0]-ancho*marco+delta
					Lb[i].xvel*=-Creb
									
				if Lb[i].y>=centro[1]+alto*marco:
					Lb[i].y=centro[1]+alto*marco-delta
					Lb[i].yvel*=-Creb
				
				if Lb[i].y<=centro[1]-alto*marco:
					Lb[i].y=centro[1]-alto*marco+delta
					Lb[i].yvel*=-Creb

	# # TECLAS ZOOM BOLAS
	# 	if keys[pygame.K_m]:
	# 		zoom+=0.01
			
	# 	if keys[pygame.K_n]:
	# 		zoom+=-0.01
			 

		if keys[pygame.K_w]:corrY+= 5
		if keys[pygame.K_s]:corrY+= -5	
		if keys[pygame.K_a]:corrX+= 5
		if keys[pygame.K_d]:corrX+= -5

		
		
		#DIBUJA BOLAS 
		for i in range(len(Lb)):

			Xzoom = (Lb[i].x-ancho/2)*marco+ancho/2
			Yzoom= (Lb[i].y-alto/2)*marco+alto/2
			Tzoom= Lb[i].tamano

			pygame.draw.circle(screen, Lb[i].color,[Xzoom+corrX, Yzoom+corrY], Tzoom, 1)
		
		
			
		
	### CARTELES TEXTOS_______________________________________________
		mouse=[Mx,My]
		#CARTEL(str(mouse),[100,200],30,WHITE)
		#CARTEL(str(fuercita),[100,200],30,WHITE)
		#CARTEL(TEXTOREBOTE,[100,100],20,WHITE)
			
	
		
		
	
		
	


  # MOVIMIENTOS______________________ 
		



		
# '''				
# # EVENTOS MOUSE_____________
	
	# #BOTON ON OFF ___________________________
			
		# if DENTROBOTON(BOTON_ON):
			# TEXTOcartel='ACTIVASTE = BOTON ON'
			# estadoplay=True
			# BOTONCLICK.play()
			# #tortaactiva=[220, 260, 20, 20]
			# on_off=[290, 20, 130, 50]
			
			
		
		# if DENTROBOTON(BOTON_OFF):
			# TEXTOcartel='ACTIVASTE = BOTON OFF'
			# BOTONCLICK.play()
			# on_off=[290, 75, 130, 55]
			# #exit()
# '''		    	
			
		
#___________________________________________________		
		
		clock.tick(500)
		
		pygame.display.flip()
	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
		
		if keys[pygame.K_q]:exit()
	
		if keys[pygame.K_p]:
			PAUSA()
	
	
	pygame.quit()


if __name__ == '__main__':
	main()











'''



  # ___________ CODIGO PARA LEER ARCHIVOS DE CARPETA 
import os
from os import listdir
from os.path import isfile, isdir

def LISTADO(path):    
    return [obj for obj in listdir(path) if isfile(path + obj)]



# PATH =  os.getcwd()
# #print(f'la carpeta es {os.getcwd()}')

# PATH+='/'

# #PATH='/home/seba/Documents/SEBA/24/PDFVOZ/'
# lista= LISTADO(PATH)
# LIST=""
# for lista in lista:
	# LIST+=lista+ '\n'	


   # FIN ________________________
   
   
   
   
   
   

	# -------- LALA ---------------------
	# LALAimagen='IMAGENES/LALA4.png'
	# LALA = pygame.image.load(LALAimagen)
	# LALA = pygame.transform.scale(LALA, (50,60))
	
	# # LALA :  Posicion  / Velocidad inicial
	# LALA_x=100
	# LALA_y=200
	
	# LALAvel_x=0.1
	# LALAvel_y=0.1 
	
	
EVENTOS CON MOUSE
		if DENTROBOTON(TORTA1) :
			BOTONCLICK.play()
			TEXTOcartel='ACTIVASTE = TORTA 1'
			tortaactiva=[TORTA1[0][0], TORTA1[0][1], 200, 60]
			#imagenfondo=TORTA1imagen
			#screen.blit(TORTA1_INVimagen, TORTA1[0])
					
		if DENTROBOTON(TORTA2) :
			BOTONCLICK.play()
			#time.sleep(0.1)
			TEXTOcartel='ACTIVASTE = TORTA 2'
			tortaactiva=[TORTA2[0][0], TORTA2[0][1], 200, 60]
			#screen.blit(TORTA2_INVimagen, [100,100])
			
			
		
		if DENTROBOTON(TORTA3) :
			BOTONCLICK.play()
			#time.sleep(0.1)
			TEXTOcartel='ACTIVASTE = TORTA 3'
			tortaactiva=[TORTA3[0][0], TORTA3[0][1], 200, 60]
			#screen.blit(TORTA2_INVimagen, [100,100])
		
		if DENTROBOTON(TORTA4) :
			BOTONCLICK.play()
			#time.sleep(0.1)
			TEXTOcartel='ACTIVASTE = TORTA 4'
			tortaactiva=[TORTA4[0][0], TORTA4[0][1], 200, 60]
			#screen.blit(TORTA2_INVimagen, [100,100])
		
		if DENTROBOTON(TORTA5) :
			BOTONCLICK.play()
			#time.sleep(0.1)
			TEXTOcartel='ACTIVASTE = TORTA 5'
			tortaactiva=[TORTA5[0][0], TORTA5[0][1], 200, 60]
			#screen.blit(TORTA2_INVimagen, [100,100])
		


def CAMBIARFONDO(archivoimagen):
	global imagenfondo
	imagenfondo = pygame.image.load(archivoimagen)
	imagenfondo = pygame.transform.scale(imagenfondo, size)
	screen.blit(imagenfondo, imagenfondo_pos)
	
	

# RELOJ ----------
	segundos+=0.005
	if int(segundos)==60:
		minutos+=1
		segundos=0
	RELOJ=f'{minutos}:{int(segundos)}'
	hora = fuente.render(str(RELOJ), 1, (0,0,0))
	screen.blit(hora, (530, 90))
	#------------------	
	
	
	
i+=1
		if (i % 2) ==0:
			pygame.mixer.pause()
			BOTONCLICK.play()
			estadopause=True
		else:
			screen.blit(PAUSEOFF, imagenfondo_pos)
			pygame.mixer.unpause()
			BOTONCLICK.play()
			estadopause=False



# BLIT -------	
	
	# SOL_pos=[SOL_x,SOL_y]
	# if P=='base' or P=='mundo-derecho' or P=='mundo-izquierdo':screen.blit(SOL,SOL_pos)
	
	# LALA_pos=[LALA_x,LALA_y]
	# screen.blit(LALA,LALA_pos)

	# CONEJO_y= 500+20*np.sin(CONEJO_x/15)
	# CONEJO_pos=[CONEJO_x,CONEJO_y]
	# if P=='casa2':
		# if CONEJOvel_x>0:
			# screen.blit(CONEJO,CONEJO_pos)
		# else:
			# screen.blit(LCONEJO,CONEJO_pos)
	
			
	
	# Draw the rectangle
	#pygame.draw.rect(screen, WHITE, [rect_x, rect_y, 50, 50])
	#pygame.draw.rect(screen, RED, [rect_x + 10, rect_y + 10, 30, 30])
	
	
	
'''
