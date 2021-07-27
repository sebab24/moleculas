# moleculas
molecular system simulation 

este script simula interaccion de atomos 

se definen (masa, carga electrica) de los atomos, 
por ejemplo 
carbon (12,-4)
nitrogeno  (  , ) 
oxigeno =  ( , ) 
hidrogeno = (1,1)

interatuan con fuerza electrica radial 
F = - q1*q2/r2   ( constante electrica = 1) 

y se mueven segun sus masa, F= m*a 

ciclos 'for' calcula la suma de todas las fuerzas sobre 1 atomo, y calcula su nueva posicion 
así repite para todas las moleculas

también agregué roce (Roc), V=*0.99 (cada vuelta del while, la vel se disminuye 0.01% )
Croc=0.99  #Coef roce al movimiento

y agregue vibracion random, 
( mov browniano), que ingresa un movimiento vibratorio pequeño de cada atomo
Cbro=0.01   # Coef movimiento Browniano

Resultados: 
Segun valores de Croc, Cbro 
se forman "moleculas"; 
H2O (Agua), CH4(metano), HCN(Cianuro), 
y a veces cadenas de C, anillos, de 5, 6 C, 


se forman moleculas tiícas que se han forman y flotan en el espacio.

sebabucc24@gmail.com









