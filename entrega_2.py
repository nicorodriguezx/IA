import itertools

from simpleai.search import (CspProblem, backtrack, min_conflicts,
                             MOST_CONSTRAINED_VARIABLE,
                             LEAST_CONSTRAINING_VALUE,
                             HIGHEST_DEGREE_VARIABLE)


slots = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q']
dominios = {slot: range(7) for slot in slots}
modulos = ['Laser', 'Motor', 'Cabina', 'Bahia de carga', 'Sistema de vida extraterrestre', 'Escudo', 'Bateria']


def limitrofes(variable):
    if variable == 'A':
        limitrofes = ['B', 'C']
    elif variable == 'B':
        limitrofes = ['A', 'D']
    elif variable == 'C':
        limitrofes = ['D', 'E']
    elif variable == 'D':
        limitrofes = ['B', 'F']
    elif variable == 'E':
        limitrofes = ['C', 'G']
    elif variable == 'F':
        limitrofes = ['D', 'H']
    elif variable == 'G':
        limitrofes = ['E', 'H', 'I']
    elif variable == 'H':
        limitrofes = ['F', 'G', 'I']
    elif variable == 'I':
        limitrofes = ['G', 'H', 'J']
    elif variable == 'J':
        limitrofes = ['I', 'K']
    elif variable == 'K':
        limitrofes = ['J', 'L']
    elif variable == 'L':
        limitrofes = ['M', 'N', 'P']
    elif variable == 'M':
        limitrofes = ['L']
    elif variable == 'N':
        limitrofes = ['L']
    elif variable == 'O':
        limitrofes = ['P']
    elif variable == 'P':
        limitrofes = ['L']
    elif variable == 'Q':
        limitrofes = ['P']

    return limitrofes


def motores(variable, value):
    if value[0] == 1:
        if (variable == 'E' or variable == 'F' or variable == 'M' or variable == 'N' or variable == 'O' or variable == 'P' or variable == 'Q'):
            return True
        else:
            return False
    else:
        return True


def repetidos(variables, values):
    slot_a, slot_b = variables
    value_a, value_b = values
    return value_a != value_b


def baterias_y_lasers(variables, values):
    value_a, value_b = values
    if (value_a == 0 and value_b == 6):
        return False
    else:
        return True


def vida_extraterrestre(variables, values):
    value_a, value_b = values
    if value_a == 4:
        if value_b == 2:
            return True
        else:
            return False
    else:
        return True


def cabinas_y_motores(variables, values):
    value_a, value_b = values
    if (value_a == 2 and value_b == 1):
        return False
    else:
        return True


def escudos_y_vida(variables, values):
    value_a, value_b = values
    if (value_a == 5 and value_b == 4):
        return False
    else:
        return True


def bahias_y_cabinas(variables, values):
    value_a, value_b = values
    if value_a == 3:
        if value_b == 2:
            return True
        else:
            return False
    else:
        return True


def baterias_y_otros(variables, values):
    if values[0] == 6:
        bat_usada = 0
        for value in values:
            if (value == 0 or value == 2 or value == 4 or value == 5):
                bat_usada += 1
        return bat_usada >= 2
    else:
        return True

restricciones = []

for slot in slots:
    restricciones.append((slot, motores))
    limit_list = limitrofes(slot)

    l = [slot]
    for limit_slot in limit_list:
        restricciones.append(((slot, limit_slot), repetidos))
        restricciones.append(((slot, limit_slot), baterias_y_lasers))
        restricciones.append(((slot, limit_slot), vida_extraterrestre))
        restricciones.append(((slot, limit_slot), cabinas_y_motores))
        restricciones.append(((slot, limit_slot), escudos_y_vida))
        restricciones.append(((slot, limit_slot), bahias_y_cabinas))
        l.append(limit_slot)
    restricciones.append(((tuple(l)), baterias_y_otros))


def resolver(metodo_busqueda, iteraciones):
    if metodo_busqueda == "backtrack":
        resultado = backtrack(CspProblem(slots, dominios, restricciones), MOST_CONSTRAINED_VARIABLE, LEAST_CONSTRAINING_VALUE)
    if metodo_busqueda == "min_conflicts":
        resultado = min_conflicts(CspProblem(slots, dominios, restricciones), iterations_limit = iteraciones)

    result = {}
    for key, value in resultado.items():
        result[key] = modulos[value]
    return result

if __name__ == '__main__':

    problema = resolver('backtrack', None)
    print problema
    problema = resolver('min_conflicts', None)
    print problema

    #resultado = backtrack(problema)
    #print resultado
    ##print 'backtrack:'
    ##imprimir(resultado)

    #resultado = min_conflicts(problema)
    #print resultado
    ##imprimir(resultado)