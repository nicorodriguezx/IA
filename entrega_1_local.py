import random
from simpleai.search import (SearchProblem, hill_climbing,
                             hill_climbing_stochastic,
                             hill_climbing_random_restarts,
                             beam,
                             simulated_annealing)
from simpleai.search.viewers import BaseViewer


#INICIAL = (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4)
INICIAL = (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9)

def lugares_vacios(state):
    posiciones = []
    for fila in range(10):
        for col in range(10):
            pos = (fila, col)
            posiciones.append(pos)
    empty = []
    for pos in posiciones:
        if pos not in state:
            empty.append(pos)
    return empty

class Hnefatafl(SearchProblem):
    def actions(self, state):
        acciones = []
        empty = lugares_vacios(state)
        for soldado in state:
            for pos in empty:
                acciones.append([soldado, pos])
        return acciones

    def result(self, state, action):
        i = 0
        nueva_lista = list(state)
        for soldado in state:
            if soldado == action[0]:
                del nueva_lista[i]
            i += 1
        nueva_lista.append(action[1])
        #print "resultado"
        return tuple(nueva_lista)

    def value(self, state):
        puntaje = 0
        for fila in range(10):
            for col in range(10):
                if (fila, col) not in state:
                    ady = []
                    ady.append((fila - 1, col))
                    ady.append((fila + 1, col))
                    ady.append((fila, col - 1))
                    ady.append((fila, col + 1))
                    suma_ady = 0
                    for pos in ady:
                        if pos in state:
                            suma_ady += 1
                    if suma_ady >= 2:
                        if (fila == 0 or fila == 9 or col == 0 or col == 9):
                            puntaje += 3
                        else:
                            puntaje += 1
        return puntaje

    def generate_random_state(self):
        estado = []
        while len(estado) != 30:
            pos = (random.randint(0, 9), random.randint(0, 9))
            if pos not in estado:
                estado.append(pos)
        return tuple(estado)

def resolver(metodo_busqueda, iteraciones, haz, reinicios):
    #problema = Hnefatafl(INICIAL)
    if metodo_busqueda == "hill_climbing":
        resultado = hill_climbing(Hnefatafl(INICIAL), iteraciones)
    if metodo_busqueda == "hill_climbing_stochastic":
        resultado = hill_climbing_stochastic(Hnefatafl(INICIAL), iteraciones)
    if metodo_busqueda == "hill_climbing_random_restarts":
        resultado = hill_climbing_random_restarts(Hnefatafl(None), reinicios, iteraciones)
    if metodo_busqueda == "beam":
        resultado = beam(Hnefatafl(INICIAL), beam_size = haz, iterations_limit = iteraciones)
    if metodo_busqueda == "simulated_annealing":
        resultado = simulated_annealing(Hnefatafl(INICIAL), iterations_limit = iteraciones)
    return resultado

if __name__ == '__main__':
    for repe in range(10):
        #result = resolver("hill_climbing", 200, None, None)
        #result = resolver("hill_climbing_stochastic", 200, None, None)
        result = resolver("beam", 200, 20, None)
        #result = resolver("hill_climbing_random_restarts", 200, None, 20)
        #result = resolver("simulated_annealing", 200, None, None)

        #hill_climbing(Hnefatafl(INICIAL))
        #print result
        #print result.value
