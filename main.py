from node import Node
from search import generalSearch

trivial = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
veryEasy = [[1, 2, 3], [4, 5, 6], [7, 0, 8]]
easy = [[1, 2, 0], [4, 5, 3], [7, 8, 6]]
doable = [[0, 1, 2], [4,5,3], [7,8,6]]
oh_boy = [[8, 7, 1], [6, 0, 2], [5, 4, 3]]
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

def main():
    puzzle = [];
    print("8-Puzzle Solver")
    print("Type '1' to use a default puzzle, or '2' for a custom one")
    choice = input()
    if choice == '1':
        print("Select a default puzzle: 1) Trivial, 2) Very Easy, 3) Easy, 4) Doable, 5) Oh Boy")
        default_choice = input()
        if default_choice == '1':
            puzzle = trivial
        elif default_choice == '2':
            puzzle = veryEasy
        elif default_choice == '3':
            puzzle = easy
        elif default_choice == '4':
            puzzle = doable
        elif default_choice == '5':
            puzzle = oh_boy
        else:
            print("Invalid choice. Please select a number from 1 to 5.")
            return
    elif choice == '2':
        print("Enter your own custom puzzle")
        print("Enter your puzzle with spaces separating each number and a 0 to represent the blank space. Please only enter valid 8-puzzles!")
        
        row1 = input("Enter row 1 (Hit enter when done)").split()
        row2 = input("Enter row 2 (Hit enter when done)").split()
        row3 = input("Enter row 3 (Hit enter when done)").split()
        custom_puzzle = [int(x) for x in row1 + row2 + row3]
    else:
        print("Invalid choice. Please select '1' or '2'.")
        return

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
