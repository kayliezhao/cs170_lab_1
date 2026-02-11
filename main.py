from node import Node
from search import generalSearch

def main():
    print("8-Puzzle Solver")
    print("Type '1' to use a default puzzle, or '2' for a custom one")
    print("Enter your puzzle with spaces separating each number and a 0 to represent the blank space. Please only enter valid 8-puzzles!")
    print("Enter row 1 (Hit enter when done)")
    input()
    print("Enter row 2 (Hit enter when done)")
    input()
    print("Enter row 3 (Hit enter when done)")
    input()

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
