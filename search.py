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


# print("Start:", problem.getStartState())
# print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
# print("Start's successors:", problem.getSuccessors(problem.getStartState()))

"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

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
    start = problem.getStartState()
    visited = set() # holds visited positions
    stack = util.Stack()    # is the fringe, the nodes to be explored
    # push the start state into the stack, add it to visited set
    stack.push([start, []])

    # while the stack is not empty, keep exploring
    while not stack.isEmpty():
        # check if the top of the stack/fringe is goal state, if so, found a
        # valid path
        curr = stack.pop()  # current node to be explored
        if (problem.isGoalState(curr[0])):  # if goal state, stop dfs
            break

        if not visited.__contains__(curr[0]):   # if not not visited, explore
            visited.add(curr[0])
            currSuccessors = problem.getSuccessors(curr[0]) # successors of curr
            for state in currSuccessors:
                route = curr[1][:]
                route.append(state[1]) # add route to get to this state
                stack.push([state[0], route])   # add path as well

    return curr[1]

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    start = problem.getStartState()
    visited = set()
    queue = util.Queue()    # bfs utilizes a queue, basically only difference
                            # between dfs and bfs
    queue.push([start, []])

    while not queue.isEmpty():
        curr = queue.pop()
        if (problem.isGoalState(curr[0])):
            break

        if not visited.__contains__(curr[0]):
            visited.add(curr[0])
            currSuccessors = problem.getSuccessors(curr[0])
            for state in currSuccessors:
                route = curr[1][:]
                route.append(state[1])
                queue.push([state[0], route])

    return curr[1]

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    start = problem.getStartState()
    visited = set()
    pq = util.PriorityQueue()   # ucs utilizes a priority queue as the fringe

    # push a list, index 0 is the position, index 1 is the route to the given
    # index 2 is the total cost of the route to the node
    pq.push([start, [], 0], 0)

    while not pq.isEmpty():
        curr = pq.pop()
        if (problem.isGoalState(curr[0])):
            break

        if not visited.__contains__(curr[0]):
            visited.add(curr[0])
            currSuccessors = problem.getSuccessors(curr[0])
            for state in currSuccessors:
                route = curr[1][:]
                route.append(state[1])
                pq.push([state[0], route, state[2] + \
                                    curr[2]], state[2] + curr[2])

    return curr[1]

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    start = problem.getStartState()
    visited = set()
    pq = util.PriorityQueue()

    pq.push([start, [], 0], 0)

    while not pq.isEmpty():
        curr = pq.pop()
        if (problem.isGoalState(curr[0])):
            break

        if not visited.__contains__(curr[0]):
            visited.add(curr[0])
            currSuccessors = problem.getSuccessors(curr[0])
            for state in currSuccessors:
                route = curr[1][:]
                route.append(state[1])
                # only difference between ucs and aStar, hCost is the heuristic
                # cost that determines when to look at the node
                hCost = heuristic(state[0], problem) + curr[2] + state[2]
                pq.push([state[0], route, state[2] + curr[2]], hCost)

    return curr[1]

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
