#node class 
class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0, heuristic_cost=0, depth=0):
        self.state = state #state of puzzle
        self.parent = parent
        self.action = action 
        self.path_cost = path_cost  # g(n)
        self.size = len(state) # size of the puzzle
        self.heuristic_cost = heuristic_cost  # h(n)
        self.depth = depth

    #compaison operator for priority queue based on f(n) = g(n) + h(n)
    def __lt__(self, other):        
        return self.path_cost + self.heuristic_cost < other.path_cost + other.heuristic_cost
    
    # equal overload operator for if it's the same    
    def __eq__(self, other):
        return self.state == other.state
    