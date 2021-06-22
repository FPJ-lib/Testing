from itertools import product

puzzle1 = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

def solve_sudoku(puzzle):
    for (row, col) in product( range(0,9), repeat=2):

        if puzzle[row][col] == 0: #Find uncalled cell
            for num in range(0,9):
                allowed = True #Check if num is allowed in row/Col/box
                for i in range(0,9):
                    if (puzzle[i][col] ==num) or (puzzle[row][i]==num):
                        allowed = False; break #Not allowed in row or col
                for (i, j) in product(range(0,3),repeat=2):
                    if puzzle[row-row%3 +i][col-col%3 +j] ==num:
                        allowed = False;break # Not allowed in box
                if allowed:
                    puzzle[row][col] = num
                    if trial := solve_sudoku(puzzle): #Solvable:
                        return trial
                    else:
                        puzzle[row][col] = 0
                    return False #Could not place a number in this cell
    return puzzle                    


def print_sudoku(puzzle):
    #Replace Zero with dashes:
    puzzle = [['*' if num ==0 else num for num in row] for row in puzzle]
    print()
    for row in range(0,9):
        if ((row%3==0) and (row != 0)):
            print(' - ' * 11 ) #Draw horizontal line
        for col in range(0,9):
            if ((col%3 ==0) and (col != 0)):
                print(' | ', end='') #Vertical line
            print('', puzzle[row][col], '',end='')
        print()
    print()


soluction = solve_sudoku(puzzle1)
print_sudoku(soluction)

print('Over')