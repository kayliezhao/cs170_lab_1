
#node class 
class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0, depth=0):
        self.state = state 
        self.parent = parent
        self.action = action  
        self.path_cost = path_cost  # g(n)
        self.depth = depth
    
    def __lt__(self, other):
        
        return self.path_cost < other.path_cost

def generalSearch(problem, queuingFunction):
    # nodes = MAKE-QUEUE(MAKE-NODE(problem.INITIAL-STATE))
    # nodes = makeQueue(makeNode(problem.initialState()))
    # while true():
    #     if not nodes:
    #         return "failure"
    #     node = removeFront(nodes)
    #     if problemGoalTest(node.state): 
    #         return node
    #     node = queuingFunction(nodes, expand(node, problem.operators))
    return


def main():
    print("8-Puzzle Solver")
    print("Type '1' to use a default puzzle, or '2' for a custom one")
    print("Enter your puzzle with spaces separating each number and a 0 to represent the blank space. Please only enter valid 8-puzzles!")
    #filler for input
    print("Enter row 1 (Hit enter when done)")
    #filler for input
    print("Enter row 2 (Hit enter when done)")
    #filler for input
    print("Enter row 3 (Hit enter when done)")

    print("Your puzzle is: ")
    #print puzzle

    print("Select an algorithm: 1) uniform cost search, 2) misplaced tile heuristic, or 3) the manhattan distance heuristic")
    #if 1 run uni search
    #elif 2 misplace
    #elif 3 manhattan
    #else please choose an option 1-3? 
    return

if __name__ == "__main__":
    main()
