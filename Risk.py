import random

class Risk:
    def __init__(self):
        while True:
            self.Jugador = input('Elige un Imperio: Imperio otomano o Imperio cristiano')        
            if self.Jugador == 'Imperio otomano' or self.Jugador == 'Imperio cristiano':
                break
            else:
                print('Nombre incorrecrto, ingresa otra vez el nombre')
            #Empezamos declarando las variables en un diccionario 
        self.imperios = {
            'Imp_otomano' : [['North Africa',0],['Egypt',0],['Middle east',0]],
            'Imp_cristiano' : [['España',0],['Francia',0],['Italia',0]]
        }

    #en la siguiente función llamaremos a la función random para sacar unos valores aleatorios del dardo
    
    def dado_Jugador(self):
        num_dado=0
        nom =  self.imperios[self.nom_origen()]
        while num_dado < 3:
            input('Pulsa en cualquier tecla para tirar el dado')
            infante = random.randint(1,7)
            print(self.imperios)
            while True:
                nombre = input('En que territorio lo desea guardar')
                a = False 
                for elem in nom:
                    print(elem)
                    if nombre in elem:
                        a = True 
                if a == True:
                    break  
            if self.Jugador == 'Imperio otomano':
                for lista in self.imperios['Imp_otomano']:
                    if lista[0] == nombre:
                        lista[1] = lista[1]+infante
            if self.Jugador == 'Imperio cristiano':
                for lista in self.imperios['Imp_cristiano']:
                    if lista[0] == nombre:
                        lista[1] = lista[1]+infante
            num_dado+=1
    # recuerda que cuando lo juntes todo cambiar el while a <3 y crear una variable para que dardo_inicial solo se aplique la primera vez
    #ahora creamos otra funcion que se encargará de jugar el turno de CPU
    
    def dado_CPU(self):
        print('Ahora es el turno del CPU')
        num_dado=0
        while num_dado < 3:
            infante = random.randint(1,7)
            if self.Jugador == 'Imperio otomano':
                nombre = random.choice([i[0] for i in self.imperios['Imp_cristiano']])
                for lista in self.imperios['Imp_cristiano']:
                    if lista[0] == nombre:
                        lista[1] = lista[1]+infante
            if self.Jugador == 'Imperio cristiano':
                nombre = random.choice([i[0] for i in self.imperios['Imp_otomano']])
                for lista in self.imperios['Imp_otomano']:
                    if lista[0] == nombre:
                        lista[1] = lista[1]+infante
            num_dado+=1
            
    #ahora definimos la función de ataque en la que nos dará los resultados de las batallas
    #en la siguiente definicion vamos a declarar una función que nos devuelve la lista correspondente al imperio elegido
    def nom_origen(self):
        if self.Jugador == 'Imperio otomano':
            return('Imp_otomano')
        else:
            return('Imp_cristiano')
        
    def nom_conquistado(self):
        if self.Jugador == 'Imperio otomano':
            return('Imp_cristiano')
        else:
            return('Imp_otomano')
        
    def Ataque(self):
        #primero pedimos al jugador elegir a que territorio quiere atacar
        print(self.imperios)
        mio =  self.imperios[self.nom_origen()]
        tuyo = self.imperios[self.nom_conquistado()]
        while True:
            conquistado = input('Elige el territorio que quieras atacar')
            print(conquistado)
            a = False 
            for elem in tuyo:
                print(elem)
                if conquistado in elem:
                    a = True 
            if a == True:
                break  
            print('Vuelve a meter el nombre del pais')
        while True:
            origen = input('Elige el pais de donde partirá tu ejercito')
            print(origen)
            b = False 
            for elem in mio:
                print(elem)
                if origen in elem:
                    b = True 
            if b == True:
                break  
            print('Vuelve a meter el nombre del pais')
                
        #ahora establecemos los calculos con sus respectivas operaciones
        pos_conq=0
        pos_og=0
        pos_ognum=0
        pos_conqnum=0
    
        for ele in self.imperios[self.nom_origen()]:
            for i in ele:
                if origen == i:
                    og_num = int(self.imperios[self.nom_origen()][pos_ognum][1])
            pos_ognum+=1
    
        for elem in self.imperios[self.nom_conquistado()]:
            for j in elem:
                if conquistado==j:
                        conq_num = int(self.imperios[self.nom_conquistado()][pos_conqnum][1])
            pos_conqnum+=1
            
        if og_num > conq_num :
            res = og_num-conq_num
            for ele in self.imperios[self.nom_conquistado()]:
                for i in ele:
                    if conquistado == i:
                        del self.imperios[self.nom_conquistado()][pos_conq]
                pos_conq+=1
            for elem in self.imperios[self.nom_origen()]:
                for i in elem:
                    if origen == i:
                        print(f'Te quedan {res} soldados')
                        num = int(input('¿Cuantos soldados quieres enviar al nuevo territorio?'))
                        self.imperios[self.nom_origen()].append([conquistado,num])
                        self.imperios[self.nom_origen()][pos_og][1] = res-num
                pos_og+=1
        elif og_num < conq_num:
            num = conq_num - og_num
            for elem in self.imperios[self.nom_conquistado()]:
                for i in elem:
                    if i == conquistado:
                        self.imperios[self.nom_conquistado()][pos_conq][1]=num
                        print(f'Quedan {num} en {self.imperios[self.nom_conquistado()][pos_conq][0]}')
                pos_conq+=1
            for elem in self.imperios[self.nom_origen()]:
                for i in elem:
                    if i == origen:
                        self.imperios[self.nom_origen()][pos_og][1]=0
                pos_og+=1
        else:
            for elem in self.imperios[self.nom_conquistado()]:
                for i in elem:
                    if i == conquistado:
                        self.imperios[self.nom_conquistado()][pos_conq][1]=0
            for elem in self.imperios[self.nom_origen()]:
                for i in elem:
                    if i == origen:
                        self.imperios[self.nom_origen()][pos_og][1]=0
                pos_og+=1
    def rondas(self, num_rondas):
        while True:
            finalizar = input('¿Quieres terminar la parrida? si o no')
            if finalizar == 'si' or finalizar == 'no':
                break
        if finalizar == 'si':
            num_rondas=0
            return num_rondas
        elif len(self.imperios[self.nom_conquistado()]) == 0:
            if self.nom_conquistado() == 'Imp_otomano':
                nombre='Imperio otomano'
            else:
                nombre = 'Imperio cristiano'
            input(f'Has ganado! lograste conquistar el imperio {nombre}')
            num_rondas=0
            print(self.imperios[self.nom_origen()])
            input('Presiona enter para terminar la partida')
            return num_rondas
        elif len(self.imperios[self.nom_origen()]) == 0:
            input(f' Upsis, Has sido derrotado')
            num_rondas=0
            print(self.imperios[nom_conquistado()])
            input('Presiona enter para terminar la partida')
            return num_rondas    
        else:
            num_rondas+=1
            return num_rondas
            

def main():
    num_rondas = 1
    partida = Risk()
    while num_rondas!=0:
        print(f'Empieza la ronda {num_rondas}')
        partida.dado_Jugador()
        partida.dado_CPU()
        partida.Ataque()
        num_rondas = partida.rondas(num_rondas)
                
if __name__ == '__main__':
    main()