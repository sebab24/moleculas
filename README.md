# moleculas
molecular system simulation 

este script simula interaccion de atomos 

se definen (masa=m, carga electrica=q) de los atomos, 
por ejemplo 
carbon (12,-4)
nitrogeno  ( 14 , 3) 
oxigeno =  (16 , -2 ) 
hidrogeno = (2,1)

interatuan con fuerza electrica radial 
F = - q1*q2/r^2   ( constante electrica = 1) 

y se mueven segun sus masa, F= m*a 

ciclos 'for' calcula la suma de todas las fuerzas sobre 1 atomo, y calcula su nueva posición 
así repite para todos los átomos

también agregué roce (Roc), V=*0.99 (cada vuelta del while, la vel se disminuye 0.01% )
Croc=0.99  #Coef roce al movimiento

y agregué vibración random, 
( mov browniano), que ingresa un movimiento vibratorio pequeño de cada átomo
Cbro=0.01   # Coef movimiento Browniano

Resultados: 
Según valores de Croc, Cbro 
se forman "moleculas"; 
H2O (Agua), CH4(metano), HCN(Cianuro), 
y a veces cadenas de C, anillos, de 5, 6 C, 


se aparecen moléculas típicas que se han forman y flotan en el espacio.

sebabucc24@gmail.com


Proxima idea: agregar una zona carga +, y carga - y hacer electrolisis
Proxima idea: en BLENDER-python, simular/visualizar movimientos/moleculas en 3d. 










