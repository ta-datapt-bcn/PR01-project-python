# Project_1_BlackJack

## Definición

Este proyecto consistirá en desarrollar código para realizar un juego interactivo entre la máquina y un jugador.

Utilizaré conocimientos de nivel básico que hemos visto al inicio de este curso. Principalmente funciones y List comprehensions.

## Pasos a seguir
### Planificación del proyecto con KANBAN

Usaré esta herramienta para estructurar el proyecto y hacer el seguimiento

### Definición del funcionamiento del juevo: Pasos y Comprobación de resultado

Antes de empezar a introducir código voy a redactar los elementos que forman el juego, las normas y la comprobación del resultado.

#### Elementos:
1. Jugadores: usuario vs máquina (Banca)
2. Baraja
3. Valor de las cartas


#### Normas:
1. Banca mezcla la baraja
2. Jugadores realizan una apuesta inicial
3. Repartir 1 carta al usuario y a la banca, boca arriba. La banca en último lugar.
4. Repartir 1 carta solamente al usuario boca arriba.
5. Turno del usuario. El usuario podrá:
        5.1 Si tiene algún As, decidir si el As vale 1 u 11
          5.2 Si las dos cartas tienen el mismo valor, podrá separar y doblar apuesta
          5.4 Pedir carta – Si  el valor total no es superior a 21. Si recibe un As debe decidir si su valor es 1 u 11
          5.5 Plantarse – mantiene el valor de sus cartas
          5.6 El jugador es eliminado si el valor de sus cartas supera 21
6.Turno de la banca: deberá pedir carta si el valor es igual o inferior a 16, y plantarse si el valor es de 17 a 21. Es eliminada si el valor es superior a 21
7. Vuelta a empezar


#### Resultado:
1. El usuario que se ha pasado de 21 no entra en el reparto 
2. Si el usuario tiene un valor más cercano a 21 que la banca
	2.1. Si es Black jack, gana apuesta x 2,5 
	2.2. Si no es Black jack, gana apuesta x 2
3. Si el usuario tiene el mismo valor que la banca, recupera la apuesta
4. Si el usuario tiene un valor más lejano a 21 que la banca, pierde la apuesta


### Desarrollo del código para ejecutar el software

Desarrollaré el código en un .ipynb para pasarlo posteriormente a un bloque de notas y guardaro como archivo Proyecto1_Carlos_Azagra.py para su ejecución desde la terminal.

Para poder ejecutar el código, el usuario tendrá dos opciones:

a) Ejecutar el archivo Proyecto1_Carlos_Azagra.py desde la terminal

b) Importando el archivo en un notebook e invocando a la función ...
