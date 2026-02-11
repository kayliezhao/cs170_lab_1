from node import Node
import heapq

# expand to generate new nodes based on curr state
def expand(node, operators):
    #filler for expand function
    return

# goal state 
def problemGoalTest(state):
    return state == [1, 2, 3, 4, 5, 6, 7, 8, 0]

# general search for taking in a problem and a queuing function 
def generalSearch(problem, queuingFunction):
    # nodes = MAKE-QUEUE(MAKE-NODE(problem.INITIAL-STATE))
    # nodes = makeQueue(makeNode(problem.initialState()))
    
    initialNode = Node(problem.initialState())

    nodes = []
    heapq.heappush(nodes, initialNode)  # (priority, node)
    # better for search
    explored = set() 

    while True:
        if not nodes:
            return "failure"
        # node = removeFront(nodes)

        node = heapq.heappop(nodes) # pop off top cuz queue
        # allows for mixing types of objects, cant change once made
        stateTuple = tuple(node.state) # convert list to tuple for set

        if stateTuple in explored:
            continue

        explored.add(stateTuple)

        if problemGoalTest(node.state): # goal state is 1 2 3 4 5 6 7 8 9 0
            return node
        
        nodes = queuingFunction(nodes, expand(node, problem.operators))
    return

#checks if the move is valid for the positions
def isValidMove(state, operator):
    blankIndex = state.index(0)
    if operator == "up":
        return blankIndex > 2 # up 0 1 2
    elif operator == "down":
        return blankIndex < 6 # down 6 7 8
    elif operator == "left":
        return blankIndex % 3 != 0 #  left 0 3 6
    elif operator == "right":
        return blankIndex % 3 != 2 # right 2 5 8 
    return False

# nodes validation to generate any possible moves for blank tile: up down left right
def expand(node, operators):
    expanded_nodes = []
    #find blank space 0
    moves = ["up", "down", "left", "right"]
    # try moving up down left right and if it's valid then create a new node with the new state and add it to expanded nodes
    blank_index = node.state.index(0)
    
    for action in moves: 

        if isValidMove(node.state, action):
            new_state = node.state.copy()
            target_index = blank_index
            
            if action == "up":
                target_index -= 3
            elif action == "down":
                target_index += 3
            elif action == "left":
                target_index -= 1
            elif action == "right":
                target_index += 1

            new_state[blank_index], new_state[target_index] = new_state[target_index], new_state[blank_index]
            #node is parent
            new_node = Node(new_state, node, action, node.path_cost + 1, 0, node.depth + 1)
            expanded_nodes.append(new_node)

    return expanded_nodes

#uniform cost search
def uniformCostSearch(problem):
    #filler
    return

#misplaced tile heuristic
def misplacedTileHeuristic(problem):
    #filler
    return

# A* manhattan distance tile heuristic
def manhattanDistanceHeuristic(problem):
    #filler
    return
