"""
Sudoku-peli.
Säännöt:

Samalla rivillä, samalla sarakkeella tai samassa ruudukossa (3x3)
ei saa olla kahta samanlaista numeroa.

-> Well-formed Sudoku with 17 - 21 symbols exist.
-> 17 is the minimum number of clues which leads to a unique solution.
"""

# To generate random numbers (integers)
import random


# Amount of starting numbers
starting_numbers = random.randint(17, 21)


# 9x9 sudoku grid template.
# "0" indicates an empty cell.
sudoku =    [[0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0]]


# Checks whether an input number is valid in the cell. Returns True or False.
def isValid(sudoku, num, row, column):
    # Check row
    for i in range(len(sudoku[0])):
        if (sudoku[row][i] == num and sudoku[column] != i):
            return False    
        
    # Check column
    for i in range(len(sudoku)):
        if (sudoku[i][column] == num and sudoku[row] != i):
            return False
        
    # Check box
    box_x = column // 3
    box_y = row // 3

    for i in range(box_y * 3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if (sudoku[i][j] == num and (i, j) != (row, column)):
                return False      
    return True


# Selects random cells from array and fills them with clue numbers.
def fill_starting_numbers(starting_numbers):
    counter = 0
    while (counter < starting_numbers): # 17 - 21 times
        while(True):
            i = random.randint(0, 8)
            j = random.randint(0, 8)
            if (sudoku[i][j] == 0): # If the cell is empty (0)
                num = random.randint(0, 9)
                if (isValid(sudoku, num, i, j)):
                    sudoku[i][j] = num
                    counter += 1
                    break


# Counts the starting clue numbers in the beginning of the game. 
def count_starting_numbers(sudoku):
    counter = 0
    for i in range(len(sudoku[0])): # Row length
        for j in range(len(sudoku)): # Column length
            if (sudoku[i][j] != 0):
                counter += 1
    return counter

    
# Solves the sudoku puzzle.
def solve(sudoku):
    find = find_empty(sudoku)
    if not find:
        return True
    else:
        i, j = find
    
    for num in range(1, 10): # Numbers from 1 - 9
        if (isValid(sudoku, num, i, j)):
            sudoku[i][j] = num
    
            if solve(sudoku):
                return True
    
            sudoku[i][j] = 0 # Backtracking algorithm

    return False


# Finds an empty cell in sudoku grid and returns its coordinate values.
# If none of the cells are empty, returns None.
def find_empty(sudoku):
    for i in range(len(sudoku[0])):
        for j in range(len(sudoku)):        
            if sudoku[i][j] == 0:
                return (i, j)  # row, col
    return None


# Prints the current state of the puzzle
def printsudoku():
    for i in range(len(sudoku)):
        line = ""
        if i == 3 or i == 6:
            print("---------------------")
        for j in range(len(sudoku[i])):
            if j == 3 or j == 6:
                line += "| "
            line += str(sudoku[i][j]) + " "
        print(line)


def main():
    fill_starting_numbers(starting_numbers)
    print("\nStarting numbers:", count_starting_numbers(sudoku))
    printsudoku()
    solve(sudoku)
    print("\nSolved")
    # print("\nSolved. There were {%d} steps in this solution.", steps_in_solution)
    printsudoku()


if "___name___" == main():
    main()