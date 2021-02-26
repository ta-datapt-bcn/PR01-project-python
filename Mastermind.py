import random

# Creamos una lista con dígitos del 0 al 9
numberlist = [0,1,2,3,4,5,6,7,8,9]

# Barajamos los elementos de la lista y seleccionamos los 4 primeros para coger 4 números del 0 al 9 al azar
# sin que se repitan
random.shuffle(numberlist)
correct = numberlist[0:4]
#print(correct)

# Ponemos falsa la variable endgame para que se ejecute mientras nadie gana
endgame = False

# Ponemos a 0 los intentos del jugador y de la máquina
attpla = 0
attcom = 0

class Player():
    """Define el jugador humano"""
    def __init__(self, nombre=None):
        if not nombre:
            nombre = input('Dime el nombre: ')
        self.nombre = nombre
        self.attpla = 0
        pass

    def attempt(self, anspla = None):

        answer = input(f'Hola {self.nombre}. Introduce tu número de 4 dígitos: ')

        # Metemos un while para que siga preguntando en caso de que no metamos 4 dígitos
        while len(answer) != 4 or not answer.isnumeric():

            if not answer.isnumeric():
                print('Has introducido algún carácter que no es un número')
                answer = input('Introduce un nuevo número de 4 dígitos sin caracteres no numéricos: ')

            elif len(answer) != 4:
                print('El número introducido no tiene 4 dígitos')
                answer = input('Introduce un nuevo número, esta vez con 4 dígitos: ')

        # Introducimos los 4 dígitos convertidos a integer en una lista (de lo contrario, los pasa como strings)
        self.anspla = [int(a) for a in answer]

        # Sumamos el intento
        self.attpla += 1

        return self.anspla

    def evaluate(self):
        # Llamamos a la variable global endgame
        global endgame
        guespla = 0
        pospla = 0

        # Este for evalúa cuántos dígitos están en la respuesta correcta
        for a in self.anspla:
            if a in correct:
                guespla += 1
        print(f'{guespla} de tus dígitos está/n contenido/s en la respuesta correcta')

        # Este for evalúa cuántos están además en la misma posición
        for x in range(0,4):
            if self.anspla[x] == correct[x]:
                pospla += 1
        print(f'{pospla} de tus dígitos está/n en la respuesta correcta y además en la misma posición')

        if self.anspla == correct:
            print(f'Enhorabuena, {self.nombre}. Has ganado tras {self.attpla} intentos')
            endgame = True

class Computer():
    """Define el jugador virtual"""
    def __init__(self, nombre='Computer'):
        self.attcom = 0
        pass

    def attempt(self, anscom = None):

        # Generamos el intento de la máquina creando una lista aleatoria con dígitos del 0 al 9 y cogiendo 4 valores
        # Igual que al principio del programa.
        # Antes lo había hecho con 'global numberlist' pero he creado una lista idéntica para evitar usar global

        numlist = [0,1,2,3,4,5,6,7,8,9]
        x = [a for a in numlist]
        random.shuffle(x)
        self.anscom = x[0:4]
        print('Turno para la máquina')
        print('Pensando')
        print(f'La elección de la máquina es {self.anscom}')

        # Sumamos el intento
        self.attcom += 1

        return self.anscom

    def evaluate(self):
        # Llamamos a la variable global endgame
        global endgame
        guescom = 0
        poscom = 0

        # Este for evalúa cuántos dígitos están en la respuesta correcta
        for a in self.anscom:
            if a in correct:
                guescom += 1
        print(f'{guescom} de los dígitos de la máquina está/n contenido/s en la respuesta correcta')

        # Este for evalúa cuántos están además en la misma posición
        for x in range(0,4):
            if self.anscom[x] == correct[x]:
                poscom += 1
        print(f'{poscom} de los dígitos de la máquina está/n en la respuesta correcta y además en la misma posición')

        if self.anscom == correct:
            print(f'Lo siento. Ha ganado la máquina tras {self.attcom} intentos')
            endgame = True

#    def attemptimproved(self):
#
#        Aquí haríamos un programa que generaría una respuesta del ordenador algo mejorada
#
#        Ej: si guescom==3, que la nueva selección incluya 3
#        Ej2: si poscom==2, que la nueva selección incluya 2 en la misma posición

a = Player()
c = Computer()

while endgame == False:
    a.attempt()
    a.evaluate()
    if endgame == False:
        c.attempt()
        c.evaluate()

# Si consiguiéramos crear la función attemptimproved para dotar a la máquina de IA, haríamos un primer intento
# a la manera tradicional y después lo haríamos con la nueva función attemptimproved:

#a.attempt()
#a.evaluate()
#if endgame == False:
#    c.attempt()
#    c.evaluate()
#
#while endgame == False:
#    a.attempt()
#    a.evaluate()
#    if endgame == False:
#        c.attemptimproved()
#        c.evaluate()
