<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# PR01-project-python
# BLACK JACK

Xabi Lopez Alfonso

## Clase Baraja

Creador de la baraja francesa con los métodos: mezclar random (barajar, valga la redundancia) y repartir cartas (pop)


## Clase Mano

**Atributos**
* nombre: para distinguir banca (CPU) del jugador
* cartas: cartas en la mano
* puntos: a los que equivalen las cartas
* AS: número de ases en la mano (para el cálculo de puntos
* blackjack: saber si la mano suma 21

**Métodos:**
* recibir:añadir carta
* calcular:calcular puntos de las cartas
* mostrar:mostrar cartas y puntos
* revelar:mostrar última carta recibida
* comprobar blackjack (BJ): saber si la mano suma 21... devuelve True/False

## Clase juego

**Atributos**
* nombre: del jugador (init)
* saldo inicial (init)


**Métodos:**
* apostar: antes de empezar cada partida, elegir el montante a jugar (menos que el saldo disponible)
* decidir: una vez repartidas las cartas, si queremos pedir otra carta o plantarnos
* continuar: al acabar una ronda, elegir si queremos jugar otra ronda o acabar el juego
* acabar: mostrar saldo restante si seguimos jugando... o que se ha acabado el saldo y se acaba el juego

| Espero que os guste el juego!|  
|:--------:|
