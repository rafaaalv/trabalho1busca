# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from collections import deque
from game import Directions
import heapq

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]
def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"

    #importa classe pilha do arquivo util.py
    from util import Stack

    #carrega o estado inicial
    start = problem.getStartState()
    #inicia a pilha
    pilha = Stack()
    #inicia a lista de visitados
    visitados = []
    #coloca na pilha o estado inicial, o caminho vazio e o custo vazio
    pilha.push((start, [], 0))

    #enquanto a pilha nao está vazia
    while not pilha.isEmpty():
        #tira o estado, caminho e custo de cima da pilha
        atual, path, custoAtual = pilha.pop()
        #adiciona o estado atual na lista de visitados
        visitados.append(atual)
        #se é o estado final, retorna o caminho e sai da função
        if problem.isGoalState(atual):
            return path
        #para todos os sucessores do estado atual, 
        for estado, ação, custo in problem.getSuccessors(atual):
            #se o estado do sucessor não está na lista de visitados
            if estado not in visitados:
                # coloca ele na pilha e introduz a ação para chegar nele no caminho
                pilha.push((estado, path + [ação], custo))
    return[]
    util.raiseNotDefined()


    
    

def breadthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    #importa classe de fila do arquivo util.py
    from util import Queue

    #inicia a fila
    queue = Queue()
    #inicia a lista de visitados
    visited = []
    #carrega o estado inicial
    start = problem.getStartState()
    #atribui ao pai do estado inicial como nulo, para facilitar a construção do caminho depois 
    parent = {
        start: (-1, -1)
    }
    #marca o estado inicial como visitado
    visited.append(start)
    #inicializa as acoes no estado inicial como uma lista vazia
    actions = {
    	start: []
    }

    #itera sobre os sucessores do estado inicial, colocando eles na fila e atribuindo o pai deles como o estado inicial
    for successor in problem.getSuccessors(start):
        queue.push(successor)
        visited.append(successor[0])    
        parent[successor[0]] = start
        actions[successor[0]] = actions[start].copy()
        actions[successor[0]].append(successor[1])

    #enquanto a fila nao está vazia
    while not queue.isEmpty():
        #tira o estado do fim da fila
        state = queue.pop()
        #encontra o pai do estado(quem colocou ele na fila)
        father = parent[state[0]]
        #se é o estado final, retorna o caminho e sai da função
        if problem.isGoalState(state[0]):
            print(actions[father] + [state[1]])
            return actions[father] + [state[1]]
        #para todos os sucessores do estado atual, 
        for successor in problem.getSuccessors(state[0]):
            #se o estado do sucessor não está na lista de visitados
            if not successor[0] in visited:
                #marca o estado do sucessor como visitado
                visited.append(successor[0])
                # coloca ele na fila e introduz a ação para chegar nele no caminho
                queue.push(successor)
                actions[successor[0]] = actions[state[0]].copy()
                actions[successor[0]].append(successor[1])
                #atribui o pai do sucessor como o estado atual
                parent[successor[0]] = state[0]
    return []
    util.raiseNotDefined()
    
def uniformCostSearch(problem):
    """
    Search the node of least total cost first.
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()
    """

    #importa classe fila de prioridade do arquivo util.py
    from util import PriorityQueue

    #carrega o estado inicial
    start = problem.getStartState()
    #inicia a fila de prioridade
    filaPrioridade = PriorityQueue()
    #inicia a lista que guardará o custo dos nodos já visitados
    visitados = {}
    #coloca na fila de prioridade o estado inicial, o caminho vazio e o custo vazio, e o custo vazio para a prioridade
    filaPrioridade.push((start, [], 0), 0)

    #enquanto a fila de prioridade nao está vazia
    while not filaPrioridade.isEmpty():
        #tira o estado, caminho e custo de cima da fila de prioridade
        atual, path, custoAtual = filaPrioridade.pop()
        #se já vimos esse estado com custo menor que o atual, ignorar
        if atual in visitados and visitados[atual] <= custoAtual:
            continue
        #caso não vimos um custo menor para chegar nesse estado, definir que esse é o custo menor para chegar nesse estado
        visitados[atual] = custoAtual
        #se é o estado final, retorna o caminho
        if problem.isGoalState(atual):
            return path
        #para todos os sucessores do estado atual, 
        for estado, ação, custo in problem.getSuccessors(atual):
            #define o novo custo como a soma do custo do sucessor mais o custo atual
            novoCusto = custo + custoAtual
            # coloca ele na fila de prioridade, introduz a ação para chegar nele no caminho e adiciona com o novo custo na fila de prioridade
            filaPrioridade.push((estado, path + [ação], novoCusto), novoCusto)
    return[]
    util.raiseNotDefined()
def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    from util import PriorityQueue
    start = problem.getStartState()
    #inicializa as acoes no estado inicial como uma lista vazia
    actions = {
    	start: []
    }
    cost = {
    	start: 0
    }
    #confere se o estado inicial eh o objetivo
    if problem.isGoalState(start):
    	return []
    #inicializa fila de prioridade e lista de visitados vazias
    queue = PriorityQueue()
    visited = []
    #coloca o estado inicial como visitado
    visited.append(start)
    #inicializa o dicionario de pais com o estado inicial sem pai
    parent = {
        start: (-1, -1)
    }
    #itera sobre os sucessores do estado inicial
    successores = problem.getSuccessors(start)
    for successor in successores:
        #atualiza o custo de g (custo acumulado) para o sucessor
        cost[successor[0]] = successor[2]
        #empurra no heap pelo valor f = g + h
        f = cost[successor[0]] + heuristic(successor[0], problem)
        queue.push(successor, f)
        #atribui o pai do sucessor como o estado inicial
        parent[successor[0]] = start
        actions[successor[0]] = actions[start].copy()
        actions[successor[0]].append(successor[1])
        #marca o estado atual como visitado
        visited.append(successor[0])
    #enquanto a fila de prioridade nao estiver vazia
    while not queue.isEmpty():
        #tira o primeiro elemento da fila (menor f)
        state = queue.pop()
        #se o estado atual for o objetivo
        if problem.isGoalState(state[0]):
            return actions[state[0]]
        else:
            #itera por seus sucessores
            successors = problem.getSuccessors(state[0])
            for successor in successors:
                #custo acumulado do caminho atual ou um custo alto se não visitado antes
                newCost = cost[state[0]] + successor[2]
                #se o sucessor ainda não foi visitado, ou houve caminho mais barato
                if successor[0] not in visited or newCost < cost[successor[0]]:
                    cost[successor[0]] = newCost
                    f = newCost + heuristic(successor[0], problem)
                    queue.push(successor, f)
                    parent[successor[0]] = state[0]
                    actions[successor[0]] = actions[state[0]].copy()
                    actions[successor[0]].append(successor[1])
                    if successor[0] not in visited:
                        visited.append(successor[0])
    #caso nao encontre o estado objetivo retorna a lista vazia
    return []
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
