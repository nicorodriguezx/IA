from simpleai.search import SearchProblem, astar, greedy, depth_first, breadth_first, limited_depth_first
from simpleai.search.viewers import BaseViewer

COSTS = {
    "up": 1,
    "down": 1,
    "left": 1,
    "right": 1,
    "attack": 1,
}

MAP = (4,4)
HE = True
BE = True
HE_POSITION = (2,2)
BE_POSITION = (4,4)

INITIAL =((0,0), HE, BE)

class MiniDota(SearchProblem):

    def actions(self, state):
        actions = []
        for action in COSTS.keys():
            state_result = self.result(state, action)
            new_x = state_result[0][0]
            new_y = state_result[0][1]
            he_res = state_result[1]
            be_res = state_result[2]
            if new_x <= MAP[0] and new_x >= 0 and new_y <= MAP[1] and new_y >= 0:
                if ((HE == True and state_result[0] == HE_POSITION) or (BE == True and state_result[0] == BE_POSITION)):
                    pass
                else:
                    if any([state[0][0] != new_x, state[0][1] != new_y, state[1] != he_res, be_res != state[2]]):
                        actions.append(action)
        return actions

    def result(self, state, action):
        x = state[0][0]
        y = state[0][1]
        he_res = state[1]
        be_res = state[2]
        if action.count("up"):
            y += 1
        if action.count("down"):
            y -= 1
        if action.count("left"):
            x -= 1
        if action.count("right"):
            x += 1
        if action.count("attack"):
            if he_res == True:
                if ((x == HE_POSITION[0] and (y == HE_POSITION[1] - 1 or y == HE_POSITION[1] + 1)) or (y == HE_POSITION[1] and (x == HE_POSITION[0] - 1 or x == HE_POSITION[0] + 1))):
                    he_res = False
            if be_res == True:
                if ((x == BE_POSITION[0] and (y == BE_POSITION[1] - 1 or y == BE_POSITION[1] + 1)) or (y == BE_POSITION[1] and (x == BE_POSITION[0] - 1 or x == BE_POSITION[0] + 1))):
                    be_res = False
        new_state = ((x, y), he_res, be_res)
        return new_state

    def is_goal(self, state):
        return state[1] == False and state[2] == False

    def cost(self, state, action, state2):
        return COSTS[action]

#def resolver(metodo_busqueda):
    #metodo = eval(metodo_busqueda)
    #if metodo_busqueda == "limited_depth_first":
        #return metodo(MiniDota(INITIAL), depth_limit=df_limit,
                      #graph_search=graph, viewer=vw, )
    #else:
        #return metodo(MiniDota(INITIAL), graph_search=graph, viewer=vw, )

def resolver(metodo_busqueda, df_limit=10, graph=False, vw=None):
    metodo = eval(metodo_busqueda)
    if metodo_busqueda == "limited_depth_first":
        return metodo(MiniDota(INITIAL), depth_limit=df_limit,
                      graph_search=graph, viewer=vw, )
    else:
        return metodo(MiniDota(INITIAL), graph_search=graph, viewer=vw, )
