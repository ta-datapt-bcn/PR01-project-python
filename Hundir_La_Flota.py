import numpy as np

#Función para definir el tamaño del tablero del juego

def tablero(tamaño):
    while tamaño < 5:
        tamaño = int(input("Entra el tamaño del tablero con el que quieres jugar (mínimo 5X5): "))
    tablero_ini = np.zeros((tamaño,tamaño), dtype = int)
    tablero = np.zeros((tamaño,tamaño), dtype = int)

    return tablero



# Definción de los jugadores mediante clases
# Metemos como a instancia de javi una referencia  a la classe tablero
class Jugadores():
    
    def __init__(self, nombre_jugador, tablero, tablero_tamaño, tiro_x, tiro_y):
        #super().__init__(nombre_barco, tamaño_barco, cantidad_barcos)
        self.nombre_jugador = nombre_jugador
        self.win = False # Esto determina en cada momento si el jugador ha ganado o no.
        self.tablero = tablero
        self.tablero_tamaño = tablero_tamaño
        self.tiro_x = tiro_x
        self.tiro_y = tiro_y

    def posicion_barcos(self):
        # Definición de la clase Barcos. Aquí se define el número de barcos y su tamaño, una vez definidos, los jugadores podran escojer donde posicionarlos:

        barcos = {"Portaaviones (5 celdas)": 5, "Buque (2 celdas)": 2, "Acorazado (4 celdas)": 4}
        barcos_posiciones = {"Portaaviones (5 celdas)": [], "Buque (2 celdas)": [], "Acorazado (4 celdas)": [], "Submarino (3 celdas)": [], "Submarino_2 (3 celdas)": []}

        for k in barcos.keys():

            coordenadas = input(f"Introduce las coordenadas iniciales (en formato letra + número, ej: A4) para el barco {k}: ")
            while coordenadas[0].isalpha() == False or coordenadas[1:].isdigit() == False:
                coordenadas = input(f"Introduce las coordenadas iniciales en el formato correcto para el barco {k}: ")

            coordenada_y = int(ord((coordenadas[0]).lower()) - 97)
            coordenada_x = int(coordenadas[1:]) -1
            direccion = input("Introduce la dirección (horizontal derecha, horizontal izquierda, veritcal arriba, vertical abajo): ")

            while direccion not in ("vertical arriba", "vertical abajo", "horizontal derecha", "horizontal izquierda"):
                direccion = input("Introduce una dirección correcta (horizontal derecha, horizontal izquierda, veritcal arriba, vertical abajo): ")        

            if direccion == "vertical arriba":
                while coordenada_y - (barcos[k]) < 0:
                    coordenadas = input(f"El barco no cabe en las celdas especificadas, vuelve a introducir las coordenadas para el barco {k} en direccion {direccion}: ")

                    while coordenadas[0].isalpha() == False or coordenadas[1].isdigit() == False:
                        coordenadas = input(f"Introduce las coordenadas iniciales en el formato correcto para el barco {k}: ")

                    coordenada_y = int(ord((coordenadas[0]).lower()) - 97)
                    coordenada_x = int(coordenadas[1:]) - 1

                for i in range(barcos[k]):
                    while self.tablero[coordenada_y - i][coordenada_x] == 1:
                        coordenadas = input(f"Dos barcos no pueden compartir una celda, vuelve a introducir las coordenadas para el barco {k} en direccion {direccion}: ")

                        while coordenadas[0].isalpha() == False or coordenadas[1].isdigit() == False:
                            coordenadas = input(f"Introduce las coordenadas iniciales en el formato correcto para el barco {k}: ")

                        coordenada_y = int(ord((coordenadas[0]).lower()) - 97)
                        coordenada_x = int(coordenadas[1:]) -1

                    self.tablero[coordenada_y - i][coordenada_x] = 1 

            elif direccion == "vertical abajo":
                while coordenada_y + barcos[k]  > self.tablero_tamaño:
                    coordenadas = input(f"El barco no cabe en las celdas especificadas, vuelve a introducir las coordenadas para el barco {k} en direccion {direccion}: ")

                    while coordenadas[0].isalpha() == False or coordenadas[1].isdigit() == False:
                        coordenadas = input(f"Introduce las coordenadas iniciales en el formato correcto para el barco {k}: ")

                    coordenada_y = int(ord((coordenadas[0]).lower()) - 97)
                    coordenada_x = int(coordenadas[1:]) - 1

                for i in range(barcos[k]):
                    while self.tablero[coordenada_y + i][coordenada_x] == 1:
                        coordenadas = input(f"Dos barcos no pueden compartir una celda, vuelve a introducir las coordenadas para el barco {k} en direccion {direccion}: ")

                        while coordenadas[0].isalpha() == False or coordenadas[1].isdigit() == False:
                            coordenadas = input(f"Introduce las coordenadas iniciales en el formato correcto para el barco {k}: ")

                        coordenada_y = int(ord((coordenadas[0]).lower()) - 97)
                        coordenada_x = int(coordenadas[1:]) -1

                    self.tablero[coordenada_y + i][coordenada_x] = 1 

            elif direccion == "horizontal derecha":
                while coordenada_x + barcos[k] > self.tablero_tamaño:
                    coordenadas = input(f"El barco no cabe en las celdas especificadas, vuelve a introducir las coordenadas para el barco {k} en direccion {direccion}: ")

                    while coordenadas[0].isalpha() == False or coordenadas[1].isdigit() == False:
                        coordenadas = input(f"Introduce las coordenadas iniciales en el formato correcto para el barco {k}: ")

                    coordenada_y = int(ord((coordenadas[0]).lower()) - 97)
                    coordenada_x = int(coordenadas[1:]) -1

                for i in range(barcos[k]):
                    while self.tablero[coordenada_y][coordenada_x + i] == 1:
                        coordenadas = input(f"Dos barcos no pueden compartir una celda, vuelve a introducir las coordenadas para el barco {k} en direccion {direccion}: ")

                        while coordenadas[0].isalpha() == False or coordenadas[1].isdigit() == False:
                            coordenadas = input(f"Introduce las coordenadas iniciales en el formato correcto para el barco {k}: ")

                        coordenada_y = int(ord((coordenadas[0]).lower()) - 97)
                        coordenada_x = int(coordenadas[1:]) -1

                    self.tablero[coordenada_y][coordenada_x + i] = 1 

            elif direccion == "horizontal izquierda":
                while coordenada_x - (barcos[k]) < 0:
                    coordenadas = input(f"El barco no cabe en las celdas especificadas, vuelve a introducir las coordenadas para el barco {k} en direccion {direccion}: ")

                    while coordenadas[0].isalpha() == False or coordenadas[1].isdigit() == False:
                        coordenadas = input(f"Introduce las coordenadas iniciales en el formato correcto para el barco {k}: ")

                    coordenada_y = int(ord((coordenadas[0]).lower()) - 97)
                    coordenada_x = int(coordenadas[1:]) -1

                for i in range(barcos[k]):
                    while self.tablero[coordenada_y][coordenada_x - i] == 1:
                        coordenadas = input(f"Dos barcos no pueden compartir una celda, vuelve a introducir las coordenadas para el barco {k} en direccion {direccion}: ")

                        while coordenadas[0].isalpha() == False or coordenadas[1].isdigit() == False:
                            coordenadas = input(f"Introduce las coordenadas iniciales en el formato correcto para el barco {k}: ")

                        coordenada_y = int(ord((coordenadas[0]).lower()) - 97)
                        coordenada_x = int(coordenadas[1:]) -1

                    self.tablero[coordenada_y][coordenada_x - i] = 1 

            tupla_posicion = (coordenada_y, coordenada_x)   
            barcos_posiciones[k].append(tupla_posicion)
            print(self.tablero)
        print("Este es tu tablero: ")
            
        return self.tablero
        
    def tiro_barco(self):
        
        tiro = input(f"Introduce las coordenadas de tiro (en formato letra + número, ej: A4): ")
        while tiro[0].isalpha() == False or tiro[1:].isdigit() == False:
            tiro = input(f"Introduce las coordenadas de manera correcta (en formato letra + número, ej: A4): ")
        
        self.tiro_y = int(ord((tiro[0]).lower()) - 97)
        self.tiro_x = int(tiro[1:]) -1
        
        while self.tiro_y > self.tablero_tamaño - 1 or self.tiro_x > self.tablero_tamaño -1 or self.tiro_y < 0 or self.tiro_x < 0:
            tiro = input(f"Coordenadas fuera del tablero! Introduce coordenadas que estén dentro del tablero (en formato letra + número, ej: A4): ")
            self.tiro_y = int(ord((tiro[0]).lower()) - 97)
            self.tiro_x = int(tiro[1:]) -1
        return self.tiro_y, self.tiro_x
        




def game():
    
    print("Bienvenido a Hundir la Flota! Empezaremos por definir los jugadores y sus respectivos tableros: ")
    
    
    nombre_1 = input("Jugador 1, introduce tu nombre: ")
    print(f"Hola {nombre_1}, a continuación deberás introducir el tamaño del tablero junto a las posiciones de tus barcos: ")

    tamaño = input(f"{nombre_1}, te toca escoger el tamaño de tablero con el que vamos a jugar (introduce un número para determinar el tamaño del tablero): ")
    
    while not tamaño.isdigit():
        tamaño = input(f"{nombre_1}, Error de formato, introduce un número")
    tamaño = int(tamaño)
    
    tablero_vacio_1 = np.zeros((tamaño,tamaño), dtype = str)
    tablero_vacio_2 = np.zeros((tamaño,tamaño), dtype = str)
    
    jugador_1 = Jugadores(nombre_1, tablero(tamaño), tamaño, 0, 0)
    jugador_1.posicion_barcos()
        
    nombre_2 = input("Jugador 2, introduce tu nombre: ")
    
    print(f"Hola {nombre_2}, a continuación deberás introducir el tamaño del tablero junto a las posiciones de tus barcos")
    
    jugador_2 = Jugadores(nombre_2, tablero(tamaño), tamaño, 0, 0)
    jugador_2.posicion_barcos()
    
    tablero1 = jugador_1.tablero
    tablero2 = jugador_2.tablero
    
    while 1 in tablero1 and 1 in tablero2:
    
        print(f"{nombre_1}, te toca!")
        print("Analiza, antes de tirar, tus tiros anteriores para asegurar un mejor tiro")
        print(tablero_vacio_2)
        jugador_1.tiro_barco()
        tiro_x_1 = jugador_1.tiro_x
        tiro_y_1 = jugador_1.tiro_y


        while tablero2[tiro_y_1, tiro_x_1] == 1:
            
            tablero2[tiro_y_1, tiro_x_1] = 0
            tablero_vacio_2[tiro_y_1, tiro_x_1] = "X"
            print("Tocado! Vuelve a tirar")
            print(tablero_vacio_2)
            if 1 in tablero2:
                jugador_1.tiro_barco()
                tiro_x_1 = jugador_1.tiro_x
                tiro_y_1 = jugador_1.tiro_y
            else:
                return print(f"Enhorabuena, {nombre_1}, has ganado!!")

        print("Agua!")
        tablero_vacio_2[tiro_y_1, tiro_x_1] = "O"


        print(f"{nombre_2}, te toca!")
        print("Analiza, antes de tirar, tus tiros anteriores para asegurar un mejor tiro")
        print(tablero_vacio_1)
        jugador_2.tiro_barco()
        tiro_x_2 = jugador_2.tiro_x
        tiro_y_2 = jugador_2.tiro_y


        while tablero1[tiro_y_2, tiro_x_2] == 1:
            
            tablero1[tiro_y_2, tiro_x_2] = 0
            tablero_vacio_1[tiro_y_2, tiro_x_2] = "X"
            print("Tocado! Vuelve a tirar")
            print(tablero_vacio_1)
            if 1 in tablero1:
                jugador_2.tiro_barco()
                tiro_x_2 = jugador_2.tiro_x
                tiro_y_2 = jugador_2.tiro_y
            else:
                return print(f"Enhorabuena, {nombre_2}, has ganado!!")

        print("Agua!")
        tablero_vacio_1[tiro_y_2, tiro_x_2] = "O"
    


if __name__ == "__main__":
	game()