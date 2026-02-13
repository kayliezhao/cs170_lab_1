from node import Node
import search

#taken from the project sample report 
trivial = [1, 2, 3, 4, 5, 6, 7, 8, 0]
veryEasy = [1, 2, 3, 4, 5, 6, 7, 0, 8]
easy = [1, 2, 0, 4, 5, 3, 7, 8, 6]
doable = [0, 1, 2, 4,5,3,7,8,6]
oh_boy = [8, 7, 1, 6 ,0 ,2 ,5 ,4 ,3]
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

def main():
    puzzle = [];
    print("8-Puzzle Solver")
    print("Type '1' to use a default puzzle, or '2' for a custom one")
    choice = input().strip()

    if choice == '1':
        print("Select a default puzzle: ")
        print("1) Trivial, ")
        print("2) Very Easy,")
        print("3) Easy, ")
        print("4) Doable, ")
        print("5) Oh Boy")
        
        default_choice = input()
        if default_choice == '1':
            puzzle = trivial
            # search.print_puzzle(puzzle)
        elif default_choice == '2':
            puzzle = veryEasy
            # search.print_puzzle(puzzle)
        elif default_choice == '3':
            puzzle = easy
            # search.print_puzzle(puzzle)
        elif default_choice == '4':
            puzzle = doable
            # search.print_puzzle(puzzle)
        elif default_choice == '5':
            puzzle = oh_boy
        else:
            print("Invalid choice. Please select a number from 1 to 5.")
            return
    elif choice == '2':
        print("Enter your own custom puzzle")
        print("Enter your puzzle with spaces separating each number")
        print("and a 0 to represent the blank space. \n Please only enter valid 8-puzzles!")
        
        row1 = input("Enter row 1 (Hit enter when done)").split()
        row2 = input("Enter row 2 (Hit enter when done)").split()
        row3 = input("Enter row 3 (Hit enter when done)").split()
        puzzle = [int(x) for x in row1 + row2 + row3]
        if sorted(puzzle) != list(range(9)):
            print("Invalid puzzle. Please enter a valid 8-puzzle with numbers 0-8 exactly once.")
            return
    else:
        print("Invalid choice. Please select '1' or '2'.")
        return

    print("Your puzzle is: ")
    #print puzzle
    problem = search.Problem(puzzle)
    search.print_puzzle(puzzle)

    print("Select an algorithm: ")
    print("1) uniform cost search, ")
    print("2) misplaced tile heuristic, or ")
    print("3) the manhattan distance heuristic")
    
    choice = input().strip()
    if choice == '1':
        search.uniformCostSearch(problem)
    elif choice == '2':
        search.misplacedTileHeuristic(problem)
    elif choice == '3':
        search.manhattanDistanceHeuristic(problem)
    else:
        print("Invalid choice. Please select an option from 1 to 3.")
        return

if __name__ == "__main__":
    main()
