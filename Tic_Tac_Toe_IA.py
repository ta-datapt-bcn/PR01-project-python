#!/usr/bin/env python
# coding: utf-8

# In[10]:


#Creación de variables
import random
jugador=1
rondas_jugadas=0
movimientos_realizados=0
posiciones=["up-L","up-M","up-R","mid-L","mid-M","mid-R","down-L","down-M","down-R"]
victoria_jugador1=0
victoria_IA=0


# In[12]:


#Creación de tablero utilizando un diccionario como estructura de datos
print("!!Bienvenidos Jugadores!!")
print(" ")
print("Instrucciones del juego:")
print(" ")
print("""Juego entre dos jugadores en los cuales estos deberán marcar diferentes casillas dentro de un cuadro
con 9 posiciones diferentes, el jugador que consiga unir un mínimo de 3 marcadores de posición ganara el juego ya sea de forma:
    - Vertical
    - Horizontal
    - Diagonal
En caso de que se completen los 9 movimientos sin que se consiga un vencedor el juego termianara en empate.""")
print("")
print("Tablero de Juego:")
print("")

tablero={"up-L":" ","up-M":" ","up-R":" ",
         "mid-L":" ","mid-M":" ","mid-R":" ",
         "down-L":" ","down-M":" ","down-R":" "}         


while True:
        print(tablero["up-L"]+"|"+tablero["up-M"]+"|"+tablero["up-R"])
        print("-+-+-")
        print(tablero["mid-L"]+"|"+tablero["mid-M"]+"|"+tablero["mid-R"])
        print("-+-+-")
        print(tablero["down-L"]+"|"+tablero["down-M"]+"|"+tablero["down-R"])
        
# Limitación de 9 movimientos en ese caso habría empate entre los jugadores
        if victoria_jugador1==1:
            print(" ")
            print("¡¡Gracias por participar!!")
            break
        elif movimientos_realizados==9:
            print(" ")
            print("El juego ha finalizado en empate, gracias por participar")
            break
            
# Arquitectura del juego        
        while True:
            if jugador==1:
                print("")
                movimiento_jugador1=input("Jugador1 ingrese su letal movimiento: ")
                if movimiento_jugador1 in tablero and tablero[movimiento_jugador1]==" ":
                    print("")
                    tablero[movimiento_jugador1]="X"
                    print("")
                    jugador=2
                    break
                
                elif movimiento_jugador1 not in posiciones:
                    print("Movimiento no válido, vuelva a intentar")
                    continue
            else:
                print("")
            
               
            #Catenaccio--> Vertical
            
                if (tablero["up-L"]=="X"and tablero["mid-L"]=="X" and tablero["down-L"]==" "):
                    tablero["down-L"]="O"
                elif (tablero["up-L"]=="X"and tablero["mid-L"]==" " and tablero["down-L"]=="X"):
                    tablero["mid-L"]="O"
                elif (tablero["up-L"]==" "and tablero["mid-L"]=="X" and tablero["down-L"]=="X"):
                    tablero["up-L"]="O"
                    
                elif (tablero["up-M"]==" "and tablero["mid-M"]=="X" and tablero["down-M"]=="X"):
                     tablero["up-M"]="O"
                elif (tablero["up-M"]=="X "and tablero["mid-M"]==" " and tablero["down-M"]=="X"):
                     tablero["mid-M"]="O"
                elif (tablero["up-M"]=="X "and tablero["mid-M"]=="X" and tablero["down-M"]==" "):
                     tablero["down-M"]="O"
                        
                elif (tablero["up-R"]=="X"and tablero["mid-R"]=="X" and tablero["down-R"]==" "):
                    tablero["down-R"]="O"
                elif (tablero["up-R"]=="X"and tablero["mid-R"]==" " and tablero["down-R"]=="X"):
                    tablero["mid-R"]="O"
                elif (tablero["up-R"]==" "and tablero["mid-R"]=="X" and tablero["down-R"]=="X"):
                    tablero["mid-R"]="O"
                
               #Catenaccio--> Vertical
            
                elif (tablero["up-L"]==" "and tablero["up-M"]=="X" and tablero["up-R"]=="X"):
                    tablero["up-L"]="O"
                elif (tablero["up-L"]=="X"and tablero["up-M"]==" " and tablero["up-R"]=="X"):
                    tablero["up-M"]="O"
                elif (tablero["up-L"]=="X"and tablero["up-M"]=="X" and tablero["up-R"]==" "):
                    tablero["up-R"]="O"
                
                elif (tablero["mid-L"]==" "and tablero["mid-M"]=="X" and tablero["mid-R"]=="X"):
                    tablero["mid-L"]="O"
                elif (tablero["mid-L"]=="X"and tablero["mid-M"]==" " and tablero["mid-R"]=="X"):
                    tablero["mid-M"]="O"
                elif (tablero["mid-L"]=="X"and tablero["mid-M"]=="X" and tablero["mid-R"]==" "):
                    tablero["mid-R"]="O"
                    
                elif (tablero["down-L"]==" "and tablero["down-M"]=="X" and tablero["down-R"]=="X"):
                    tablero["down-L"]="O"
                elif (tablero["down-L"]=="X"and tablero["down-M"]==" " and tablero["down-R"]=="X"):
                    tablero["down-M"]="O"
                elif (tablero["down-L"]=="X"and tablero["down-M"]=="X" and tablero["down-R"]==" "):
                    tablero["down-R"]="O"
            
                
                #Catenaccio--> Diagonal
                
                elif (tablero["up-L"]==" "and tablero["mid-M"]=="X" and tablero["down-R"]=="X"):
                    tablero["up-L"]="O"
                elif (tablero["up-L"]=="X"and tablero["mid-M"]==" " and tablero["down-R"]=="X"):
                    tablero["mid-M"]="O"
                elif (tablero["up-L"]=="X"and tablero["mid-M"]=="X" and tablero["down-R"]==" "):
                    tablero["down-R"]="O"
                    
                elif (tablero["up-R"]==" "and tablero["mid-M"]=="X" and tablero["down-L"]=="X"):
                    tablero["up-R"]="O"
                elif (tablero["up-R"]=="X"and tablero["mid-M"]==" " and tablero["down-L"]=="X"):
                    tablero["mid-M"]="O"
                elif (tablero["up-R"]=="X"and tablero["mid-M"]=="X" and tablero["down-L"]==" "):
                    tablero["down-L"]="O"
                    
                    
                
                else:
                    print("")
                    tablero[random.choice(list(tablero.keys()))]="O"
                    print(" ")
                    print("")
                jugador=1

                break  
    
        movimientos_realizados+=1
        print("-----------","Movimiento número: ", movimientos_realizados,"-----------")
        print("")
   
          #Combinación ganadora--> Vertical

        if (tablero["up-L"]=="X"and tablero["mid-L"]=="X" and tablero["down-L"]=="X"):
            victoria_jugador1+=1
            print("¡¡Juego terminado, Jugador1 es el real champion!!")
            print(" ")
            
        if (tablero["up-M"]=="X"and tablero["mid-M"]=="X" and tablero["down-M"]=="X"):
            victoria_jugador1+=1
            print("¡¡Juego terminado, Jugador1 es el real champion!!")
            print(" ")

        if (tablero["up-R"]=="X"and tablero["mid-R"]=="X" and tablero["down-R"]=="X"):
            victoria_jugador1+=1
            print("¡¡Juego terminado, Jugador1 es el real champion!!")
            print(" ")

        if (tablero["up-L"]=="O"and tablero["mid-L"]=="O" and tablero["down-L"]=="O"):
            victoria_IA=0
            print("¡¡Juego terminado, la IA es la real champion!!")
            print(" ")

        if (tablero["up-M"]=="O"and tablero["mid-M"]=="O" and tablero["down-M"]=="O"):
            victoria_IA=0
            print("¡¡Juego terminado, IA es el real champion!!")
            print(" ")

        if (tablero["up-R"]=="O"and tablero["mid-R"]=="O" and tablero["down-R"]=="O"):
            victoria_IA=0
            print("¡¡Juego terminado, IA es el real champion!!")
            print(" ")



        #Combinación ganadora--> Horizontal  

        if (tablero["up-L"]=="X"and tablero["up-M"]=="X" and tablero["up-R"]=="X"):
            victoria_jugador1+=1
            print("¡¡Juego terminado, Jugador1 es el real champion!!")
            print(" ")

        if (tablero["mid-L"]=="X"and tablero["mid-M"]=="X" and tablero["mid-R"]=="X"):
            victoria_jugador1+=1
            print("¡¡ Juego terminado, Jugador1 es el real champion !!")
            print(" ")

        if (tablero["down-L"]=="X"and tablero["down-M"]=="X" and tablero["down-R"]=="X"):
            victoria_jugador1+=1
            print("¡¡Juego terminado, Jugador1 es el real champion!!")
            print(" ")

        if (tablero["up-L"]=="O"and tablero["up-M"]=="O" and tablero["up-R"]=="O"):
            victoria_IA=0
            print("¡¡Juego terminado, la IA es la real champion!!")
            print(" ")

        if (tablero["mid-L"]=="O"and tablero["mid-M"]=="O" and tablero["mid-R"]=="O"):
            victoria_IA=0
            print("¡¡Juego terminado, IA es el real champion!!")
            print(" ")

        if (tablero["down-L"]=="O"and tablero["down-M"]=="O" and tablero["down-R"]=="O"):
            victoria_IA=0
            print("¡¡Juego terminado, IA es el real champion!!")
            print(" ")


        #Combinación ganadora--> Diagonal

        if (tablero["up-L"]=="X"and tablero["mid-M"]=="X" and tablero["down-R"]=="X"):
            victoria_jugador1+=1
            print("¡¡Juego terminado, Jugador1 es el real champion!!")
            print(" ")

        if (tablero["up-R"]=="X"and tablero["mid-M"]=="X" and tablero["down-L"]=="X"):
            victoria_jugador1+=1
            print("¡¡Juego terminado, Jugador1 es el real champion!!")
            print(" ")

        if (tablero["up-L"]=="O"and tablero["mid-M"]=="O" and tablero["down-R"]=="O"):
            victoria_IA=0
            print("¡¡Juego terminado, la IA es la real champion!!")
            print(" ")

        if (tablero["up-R"]=="O"and tablero["mid-M"]=="O" and tablero["down-L"]=="O"):
            victoria_IA=0
            print("¡¡Juego terminado, la IA es la real champion!!")
            print(" ")
           


# In[ ]:




