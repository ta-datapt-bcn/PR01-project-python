import random
        

class Baraja:
    def __init__(self):
        spade = "♠"
        heart = "♥"
        diamond = "♦"
        club = "♣"
        palos = [spade, heart, diamond, club]
        numeros = [i for i in range(2,11)]+["J", "Q", "K", "A"]
        self.baraja = [(palos, numeros) for palos, numeros in zip(palos*len(numeros), numeros*len(palos))]        
    
    def mezclar(self):
        if (self.baraja):
            random.shuffle(self.baraja)
    
    def repartir(self):
        if len(self.baraja)>0:
            self.carta = self.baraja.pop()
            return self.carta


class Mano:
    def __init__(self, nombre="banca"):
        self.nombre = nombre
        self.cartas = []
        self.puntos = 0
        self.AS = 0
        self.blackjack = False
        
    def recibir(self, carta):
        self.cartas.append(carta)
    
    def calcular(self):
        self.puntos = 0
        self.AS = 0
        for i in self.cartas:
            if i[1] in ["J", "Q", "K"]:
                self.puntos += 10
            elif i[1]=="A":
                self.puntos += 11
                self.AS += 1
            else:
                self.puntos += i[1]
        if self.puntos>21 and self.AS>0:
            self.puntos -= 10
            self.AS -= 1
        else:
            pass
        return self.puntos
    
    def mostrar(self):
        print(f'\nCartas {self.nombre}: {self.cartas}')
        print(f'\nValor {self.nombre}: {self.calcular()}\n')
        
    def revelar(self):
        print(f'\nCarta recibida {self.nombre}: {self.cartas[-1]}')
    
    def comprobarBJ(self):
        if (len(self.cartas)==2) and (self.puntos == 21):
            self.blackjack = True
        else:
            pass
        return self.blackjack


class Juego:
    def __init__(self):
        self.nombre = input("BIENVENID@ AL CASINO DE XABI... A ver si consigues no perderlo todo ;)\n\n>>>>> Introduce tu nombre: ")
        if self.nombre =='':
            self.nombre = "jugador"
        else:
            pass
        self.otra = True
        while True:
            try:
                self.saldo = float(input("\n>>>>> Introduce tu saldo (€): "))
                if self.saldo<=0:
                    raise ValueError
                break
            except:
                print("\n\tIntroduce un número positivo")

    def decidir(self):
        self.accion = str(input("\n>>>>> Elige carta (C) o  plantarte (P): ").lower())
        while self.accion not in ["c", "p"]:
            self.accion = str(input("\n\tEscribe C para carta o P para plantarte").lower())
        return self.accion
    
    def continuar(self):
        self.decision = str(input("\n>>>>> Continuar? SI o  NO: ").lower())
        while self.decision not in ["si", "no"]:
            self.decision = str(input("\n>>>>> Escribe SI para continuar o NO para acabar el juego: ").lower())
        if self.decision=="si":
            self.otra = True
        else:
            self.otra = False
        return self.decision
    
    def acabar(self):
        if self.saldo>0:
            print(f'\n... tu saldo restante es de {self.saldo}€')
            self.continuar()
        else:
            print("\nOh que pena, no tienes más saldo...")

    def apostar(self):
        while True:
            try:
                self.apuesta = float(input(f"\n>>>>> Apuesta ronda {self.ronda} (menos de {self.saldo}€): "))
                if (self.apuesta>self.saldo) or (self.apuesta<=0):
                    raise ValueError
                break
            except:
                print(f"\n\tIntroduce un número menor a {self.saldo}")
        return self.apuesta


    def jugar(self):
        self.saldo_inicial = self.saldo
        print(f'\nBienvenid@ {self.nombre}, no olvides jugar con responsabilidad (y no perderlo todo)')
        self.ronda = 1
        while self.saldo>0 and self.otra == True:
            print("________________________________________________________________________________________")
            print(f"\nArranca la {self.ronda}ra RONDA")
            self.jugada=self.apostar()
            
            self.baraja = Baraja()
            self.baraja.mezclar()
            
            print(f'\nReparto inicial de cartas...')
            
            self.banca = Mano()
            [self.banca.recibir(self.baraja.repartir()), self.banca.recibir(self.baraja.repartir())]
            print(f'\nCarta visible banca {self.banca.cartas[0]}')
            self.banca.calcular()
            self.banca.comprobarBJ()

            self.jugador = Mano(self.nombre)
            [self.jugador.recibir(self.baraja.repartir()),self.jugador.recibir(self.baraja.repartir())]
            self.jugador.mostrar()
            self.jugador.comprobarBJ()
            
            print('\n------------------------------')
            
            if self.jugador.blackjack or self.banca.blackjack:
                self.banca.mostrar()
                if self.jugador.blackjack and self.banca.blackjack:
                    print("\nEmpate a blackjacks!")
                    self.saldo = self.saldo
                elif self.jugador.blackjack:
                    print(f"\nBlackjack de {self.nombre}!")
                    self.saldo += self.jugada*1.5
                else:
                    print(f"\nBlackjack de la banca!")
                    self.saldo -= self.jugada
                print('\n------------------------------')
                
            else: 
                self.decision = self.decidir()    
                while self.decision=="c":
                    self.jugador.recibir(self.baraja.repartir())
                    self.jugador.revelar()
                    self.jugador.mostrar()
                    print('\n------------------------------')
                    if self.jugador.calcular() < 21:
                        self.decision = self.decidir()
                    elif self.jugador.calcular() == 21:
                        self.decision = "p"
                    else:
                        break
                else:
                    print(f'\nCarta oculta banca {self.banca.cartas[1]}')
                    self.banca.mostrar()
                    print('\n------------------------------')
                    while self.banca.calcular()<self.jugador.calcular():
                        self.banca.recibir(self.baraja.repartir())
                        self.banca.revelar()
                        self.banca.mostrar()
                        print('\n------------------------------')
                        if self.banca.calcular()>21:
                            break
                        else:
                            pass
            
                if (self.jugador.calcular()>21) or (self.banca.calcular()>21):
                    if (self.jugador.calcular()>21):
                        print(f"\nPierde {self.nombre} por sumar +21... Gana la banca!")
                        self.saldo -= self.jugada
                    else:
                        print(f"\nPierde banca por sumar +21... Gana {self.nombre}!")
                        self.saldo += self.jugada
                else:
                    if self.banca.puntos>self.jugador.puntos:
                        print("\nGana la banca por tener un valor de cartas más alto!")
                        self.saldo -= self.jugada
                    elif self.banca.puntos<self.jugador.puntos:
                        print(f"\nGana {self.nombre} por tener un valor de cartas más alto!")
                        self.saldo += self.jugada
                    else:
                        print(f"\nEmpate!")
                        self.saldo = self.saldo

            self.acabar()
            self.ronda += 1
            
        print("________________________________________________________________________________________")
        
        if self.saldo==0:
            print(f'\nGracias por participar {self.nombre}, hoy lo has perdido todo... Vuelve otro dia mejor!')
        else:
            self.dinero = self.saldo-self.saldo_inicial
            if self.dinero > 0:
                print(f'\nGracias por participar {self.nombre}, has ganado {self.dinero}€')
            elif self.dinero < 0:
                print(f'\nGracias por participar {self.nombre}, has perdido {-self.dinero}€')
            else:
                print(f'\nGracias por participar {self.nombre}, te quedas con tu saldo incial de {self.saldo_inicial}€')
        
        print(f'\n\nHasta pronto!\n\n© 1992-2021 CASINO DE XABI Todos los derechos reservados.')    


def main():
	Juego().jugar()

if __name__ == "__main__":
	main()