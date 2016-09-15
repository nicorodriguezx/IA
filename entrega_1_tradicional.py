from simpleai.search import breadth_first, depth_first, greedy, astar, SearchProblem
from simpleai.search.viewers import BaseViewer
import collections

def t2l(t):
    return list(list(r) for r in t)


def l2t(l):
    return tuple(tuple(r) for r in l)


enemy_pos = [[0, 0], [0, 2], [0, 4], [0, 6],
[1, 4],
[2, 0],
[3, 1], [3, 6], [3, 7], [3, 9],
[4, 0], [4, 7], [4, 8],
[5, 4], [5, 9],
[6, 0], [6, 5], [6, 9],
[7, 0], [7, 7],
[8, 2], [8, 4], [8, 9],
[9, 1], [9, 4], [9, 6], [9, 7]]

limit_pos = []
for pos in enemy_pos:
    if pos[0] > 0:
        limit_pos.append([pos[0] - 1, pos[1]])
    if pos[0] < 9:
        limit_pos.append([pos[0] + 1, pos[1]])
    if pos[1] > 0:
        limit_pos.append([pos[0], pos[1] - 1])
    if pos[1] < 9:
        limit_pos.append([pos[0], pos[1] + 1])

blocked_pos = [item for item, count in collections.Counter(l2t(limit_pos)).items() if count > 1]
blocked_pos = set(l2t((t2l(blocked_pos) + enemy_pos)))




class Hnefatafl(SearchProblem):
    def cost(self, state1, action, state2):
        return 1

    def is_goal(self, state):
        #print state
        if state not in blocked_pos:
            if state[0] == 0 or state[0] == 9:
                return True
            elif state[1] == 0 or state[1] == 9:
                return True
            else:
                return False

    def actions(self, state):
        acciones = []
        fila = state[0]
        columna = state[1]
        if state[0] > 0:
            if (fila - 1, columna) not in blocked_pos:
                acciones.append([fila - 1, columna])
        if state[0] < 9:
            if (fila + 1, columna) not in blocked_pos:
                acciones.append([fila + 1, columna])
        if state[1] > 0:
            if (fila, columna - 1) not in blocked_pos:
                acciones.append([fila, columna - 1])
        if state[1] < 9:
            if (fila, columna + 1) not in blocked_pos:
                acciones.append([fila, columna + 1])
        return acciones

    def result(self, state, action):
        state = list(state)
        state = action
        state = tuple(state)
        return state

    def heuristic(self, state):
        total = state[0]
        if  9 - state[0] < total:
            total = 9 - state[0]
        if state[1] < total:
            total = state[1]
        if  9 - state[1] < total:
            total = 9 - state[1]
        return total

def resolver(metodo_busqueda, posicion_rey, controlar_estados_repetidos):
    visor = BaseViewer()
    metodo = eval(metodo_busqueda)
    problema = Hnefatafl(posicion_rey)
    resultado = metodo(problema, viewer=visor, graph_search=controlar_estados_repetidos)

    print 'Estado meta:'
    print resultado.state
    print 'Camino:'
    print len(resultado.path())
    for accion, estado in resultado.path():
        print 'Movi a', estado
    print visor.stats

    return resultado

if __name__ == '__main__':
    resolver("greedy", (5, 3), False)