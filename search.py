from node import Node
import heapq

grid_size = 3 # for 8 puzzle, grid size is 3x3

# goal state 
def problemGoalTest(state):
    n = grid_size * grid_size
    goal_state = list(range(1, n)) + [0]
    return state == goal_state

# problem class to hold initial state and operators
class Problem:
    def __init__(self, initial_state):
            self.initial_state = initial_state
            self.operators = None
        
    def initialState(self):  
        return self.initial_state

# general search for taking in a problem and a queuing function 
def generalSearch(problem, queuingFunction):
    # nodes = MAKE-QUEUE(MAKE-NODE(problem.INITIAL-STATE))
    initialNode = Node(problem.initialState())

    nodes = []
    heapq.heappush(nodes, initialNode)  # (priority, node)
    # better for search
    visited = set() 
    while True:
        if not nodes:
            return "failure"

        node = heapq.heappop(nodes) # pop off top cuz queue
        # allows for mixing types of objects, cant change once made
        stateTuple = tuple(node.state) # convert list to tuple for set

        if stateTuple in visited:
            continue
        visited.add(stateTuple)

        if problemGoalTest(node.state): # goal state is 1 2 3 4 5 6 7 8 9 0
            return node
        
        nodes = queuingFunction(nodes, expand(node, problem.operators))
    return

#checks if the move is valid for the positions
def isValidMove(state, operator):
    blankIndex = state.index(0)
    if operator == "up":
        return blankIndex >= grid_size # up 0 1 2
    elif operator == "down":
        return blankIndex < len(state)-grid_size # down 6 7 8
    elif operator == "left":
        return blankIndex % grid_size != 0 #  left 0 3 6
    elif operator == "right":
        return blankIndex % grid_size != grid_size - 1 # right 2 5 8 
    return False

# nodes validation to generate any possible moves for blank tile: up down left right
def expand(node, operators):
    expanded_nodes = []
    #find blank space 0
    moves = ["up", "down", "left", "right"]
    # try moving up down left right and if it's valid then create a new node with the new state and add it to expanded nodes
    blank_index = node.state.index(0)
    
    # checking if each move is a valid move
    # if valid then create new state
    for action in moves: 
        if isValidMove(node.state, action):
            new_state = node.state.copy()
            target_index = blank_index
            
            if action == "up":
                target_index -= grid_size
            elif action == "down":
                target_index += grid_size
            elif action == "left":
                target_index -= 1
            elif action == "right":
                target_index += 1

            new_state[blank_index], new_state[target_index] = new_state[target_index], new_state[blank_index]
            #node is parent
            new_node = Node(new_state, node, action, node.path_cost + 1, 0, node.depth + 1)
            expanded_nodes.append(new_node)

    return expanded_nodes

#uniform cost search expand cheapest node, cost = path cost g(n)
def uniformCostSearch(problem):
    start_node = Node(problem.initialState())
    start_node.heuristic_cost = 0
    max_queue_size = 0
    nodes_expanded = 0
    nodes = []

    heapq.heappush(nodes, start_node)    
    visited = set()

    # visiting nodes
    while nodes:
        max_queue_size = max(max_queue_size, len(nodes))   

        curr_node = heapq.heappop(nodes)
        state_tuple = tuple(curr_node.state)

        if state_tuple in visited:
            continue

        visited.add(state_tuple)

        # print trace
        print(f"The best state to expand with a g(n) = {curr_node.depth} and h(n) = {curr_node.heuristic_cost} is…")
        print_puzzle(curr_node.state)

        if problemGoalTest(curr_node.state):
            # print final stats
            print("End of search!")
            print(f"Solution depth was {curr_node.depth}")
            print(f"Number of nodes expanded: {nodes_expanded}")
            print(f"Max queue size: {max_queue_size}")
            return curr_node
        
        nodes_expanded += 1

        if problemGoalTest(curr_node.state):
            return curr_node
        
        children = expand(curr_node, problem.operators)
        
        for child in children: #set heuristic cost to 0 for uniform cost search
            child.heuristic_cost = 0
            heapq.heappush(nodes, child)
    return "failure"

# misplaced tile heuristic helper function
def misplacedTileHeuristic(state):
    count = 0
    for i in range(len(state)):
        if state[i] != 0:  # skip blank
            if state[i] != i + 1:
                count += 1
    return count
# a star misplaced tile heuristic
def aStarMisplacedTileHeuristic(problem):
    start_node = Node(problem.initialState())
    start_node.heuristic_cost = misplacedTileHeuristic(start_node.state)
    max_queue_size = 0
    nodes_expanded = 0
    nodes = []

    heapq.heappush(nodes, start_node)
    visited = set()

    # visiting nodes
    while nodes:
        curr_node = heapq.heappop(nodes)
        state_tuple = tuple(curr_node.state)
        if state_tuple in visited:
            continue
        visited.add(state_tuple)

        #print trace
        print(f"The best state to expand with a g(n) = {curr_node.depth} and h(n) = {curr_node.heuristic_cost} is…")
        print_puzzle(curr_node.state)

        if problemGoalTest(curr_node.state):
            # Print final stats
            print("End of search!")
            print(f"Solution depth was {curr_node.depth}")
            print(f"Number of nodes expanded: {nodes_expanded}")
            print(f"Max queue size: {max_queue_size}")
            return curr_node
        
        nodes_expanded += 1

        if problemGoalTest(curr_node.state): # check if curr node is goal state before expanding
            return curr_node
        children = expand(curr_node, problem.operators)
        for child in children:
            child.heuristic_cost = misplacedTileHeuristic(child.state)
            heapq.heappush(nodes, child)
    return "failure"
#helper function to calculate manhattan distance heuristic
def manhattanDistanceHeuristic(state):
    distance = 0
    
    # iterate thru each tile to calculate total manhattan distance
    for i in range(len(state)): 
        if state[i] != 0: #skip blank tile
            curr_row = i // grid_size
            curr_col = i % grid_size
            
            goal_index = state[i] - 1
            goal_row = goal_index // grid_size
            goal_col = goal_index % grid_size
            
            #add distance tile needs to travel with the total
            distance += abs(curr_row - goal_row) + abs(curr_col - goal_col)
    return distance

# A* manhattan distance tile heuristic
def aStarManhattanDistanceHeuristic(problem):
    start_node = Node(problem.initialState())
    start_node.heuristic_cost = manhattanDistanceHeuristic(start_node.state)
    nodes = []
    nodes_expanded = 0
    max_queue_size = 0
    heapq.heappush(nodes, start_node)
    visited = set()

    # search as long as there are nodes to expand
    while nodes:
        curr_node = heapq.heappop(nodes)
        state_tuple = tuple(curr_node.state)
        if state_tuple in visited:
            continue
        visited.add(state_tuple)

        #print trace
        print(f"The best state to expand with a g(n) = {curr_node.depth} and h(n) = {curr_node.heuristic_cost} is…")
        print_puzzle(curr_node.state)

        if problemGoalTest(curr_node.state):
            # Print final stats
            print("End of search!")
            print(f"Solution depth was {curr_node.depth}")
            print(f"Number of nodes expanded: {nodes_expanded}")
            print(f"Max queue size: {max_queue_size}")
            return curr_node
        
        nodes_expanded += 1

        if problemGoalTest(curr_node.state): #calculate manhattan distance heuristic before adding to queue
            return curr_node
        children = expand(curr_node, problem.operators)
        for child in children:
            child.heuristic_cost = manhattanDistanceHeuristic(child.state)
            heapq.heappush(nodes, child)
    return "failure"

#prints the puzzle
def print_puzzle(state):
    for i in range(0, len(state), grid_size):
        print(state[i:i+grid_size])
    print()

