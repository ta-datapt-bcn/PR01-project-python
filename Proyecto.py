#!/usr/bin/env python
# coding: utf-8

# ## Código y ejecución de 3 en Raya

# In[ ]:


# %load 3enRaya.py
import math
import random
tablero=[]  #Nuestro tablero inicalmente serán nueva callisas vacias
casillasVacias=[]
TABLERO_FILAS=3
TABLERO_COLUMNAS=3
random.seed(5)

#inicializamos el tablero
for i in range(9):
   tablero.append(' ')
   casillasVacias.append(i)

#Colaca una ficha en el tablero
def numero(literal, inferior, superior):
   while True:
      valor=input(literal)
      while(not valor.isnumeric()):
         print("Solo se adminten números entre {0} y {1}".format(inferior,superior))
         valor=input(literal)
      coor=int(valor)
      if(coor>=inferior and coor<=superior):
         return coor

      else:
         print("El valor indicado es incorrecto, introduzca un número entre {0} y {1}".format(inferior,superior))
def numeroHermanos(casilla, ficha, v, h):
   f=math.floor(casilla/TABLERO_COLUMNAS) #Obtengo la fila
   c=casilla % TABLERO_COLUMNAS #columna
   fila_nueva=f+v
   if(fila_nueva<0 or fila_nueva>=TABLERO_FILAS):
      return 0
   columna_nueva=c+h
   if(columna_nueva<0 or columna_nueva>=TABLERO_COLUMNAS):
      return 0
#No estamos en el limite así que
#calculamos la nueva posición y vemos si hay la misma ficha
   pos=(fila_nueva*TABLERO_COLUMNAS+columna_nueva)
   if(tablero[pos]!=ficha):
      return 0
   else:
      return 1+numeroHermanos(pos,ficha,v,h)

#comprobamos que la ficha colocada en la casilla indica tiene dos fichas similares en casillas contiguas
def hemosGanado(casilla, ficha):
   hermanos=numeroHermanos(casilla,ficha,-1,-1)+numeroHermanos(casilla,ficha,1,1)
   if(hermanos==2):
      return True
   hermanos=numeroHermanos(casilla,ficha,1,-1)+numeroHermanos(casilla,ficha,-1,1)
   if(hermanos==2):
      return True
   hermanos=numeroHermanos(casilla,ficha,-1,0)+numeroHermanos(casilla,ficha,1,0)
   if(hermanos==2):
      return True
   hermanos=numeroHermanos(casilla,ficha,0,-1)+numeroHermanos(casilla,ficha,0,1)
   if(hermanos==2):
      return True

def colocarFicha(ficha):
   print("Dame la posición de una ficha")
   while True:
      fila=numero("Fila entre [1 y 3]: ", 1,3)-1 #Restamos uno ya que nuestro rango real está entre 0 y 2
      columna=numero("Columna entre [1 y 3]: ",1,3)-1
      #Como mi tablero es de 3x3
      casilla=fila*TABLERO_COLUMNAS+columna
      if(tablero[casilla]!=' '):
         #Esa casilla ya está cubierta
         print("La casilla está ocupada")
      else:
         tablero[casilla]=ficha
         return casilla
def colocarFichaMaquina(ficha, fichaContrincante):
   random.shuffle(casillasVacias)
   despiste=random.randint(0,100)
   
   if(despiste<30):
      for casilla in casillasVacias:
         if(hemosGanado(casilla,ficha)):
            tablero[casilla]=ficha
            return casilla
      for casilla in casillasVacias:
         if(hemosGanado(casilla,fichaContrincante)):
            tablero[casilla]=ficha
            return casilla
   else:
      print("Ufff, me he despistado")
   for casilla in casillasVacias:
      tablero[casilla]=ficha
      return casilla

def pintarTablero():
   pos=0
   print(("-"*18))
   for fila in range(3):
      for columna in range(3):
         print("| ",tablero[pos]," ", end="")
         pos+=1
      print("|\n",("-"*18))




jugadores=[]
numeroJugadores=numero("Numero de jugadores: ",0,2)
for i in range(numeroJugadores):
   jugadores.append({"nombre":input("Nombre del jugador "+str(i+1)+": "),"tipo":"H"})
for i in range(2-numeroJugadores):
   jugadores.append({"nombre":"Maquina "+str(i+1),"tipo":"M"})

print("\n Empezamos la partida con los jugadores")
for jugador in jugadores:
   print("\t",jugador["nombre"])

empieza=numero("¿Que jugador empieza? [1="+jugadores[0]["nombre"]+",2="+jugadores[1]["nombre"]+"]: ",1,2)
if(empieza==2):
   jugadores.reverse()
#Inikciamos el juego
continuar=True
fichasEnTablero=0
while continuar:
   #Pedimos posición de la ficha
   pintarTablero()
   numJugador=(fichasEnTablero&1)
   ficha='X' if numJugador==1 else 'O'
   if(jugadores[numJugador]["tipo"]=="H"):
      casilla=colocarFicha(ficha)
   else:
      casilla=colocarFichaMaquina(ficha,'X' if numJugador==0 else 'O')
   casillasVacias.remove(casilla)
   if(hemosGanado(casilla,ficha)):
      continuar=False
      print(jugadores[numJugador]["nombre"],"¡¡¡¡¡Has ganado!!!!")
   fichasEnTablero+=1
   if(fichasEnTablero==9):
      continuar=False
      print("TABLAS")
pintarTablero()


# In[ ]:


get_ipython().run_line_magic('run', '3enRaya.py')


# In[ ]:




