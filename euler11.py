import numpy as np

grid = []

for i in range(20):
    grid.append(raw_input().split())
#finish your entry by pressing ctrl+D


def max_row_product():

    maxProduct = 0

    for i in range(0,20,1):

        for j in range(0,17,1):
            prod = int(grid[i][j])*int(grid[i][j+1])*int(grid[i][j+2])*int(grid[i][j+3])

            if maxProduct < prod:
                maxProduct = prod

    return maxProduct


def max_column_product():

    maxProduct = 0

    for j in range(0,20,1):

        for i in range(0,17,1):
            prod = int(grid[i][j])*int(grid[i+1][j])*int(grid[i+2][j])*int(grid[i+3][j])

            if maxProduct < prod:
                maxProduct = prod

    return maxProduct


def max_diagonal_1_product():

    maxProduct = 0

    for j in range(3,20,1):

        for i in range(0,j-2,1):

            prod = int(grid[i][j])*int(grid[i+1][j-1])*int(grid[i+2][j-2])*int(grid[i+3][j-3])
            if maxProduct < prod:
                maxProduct = prod

    return maxProduct


def max_diagonal_2_product():

    maxProduct = 0

    for j in range(1,17,1):

        for i in range(19,j-2,-1):

            prod = int(grid[i][j])*int(grid[i-1][j+1])*int(grid[i-2][j+2])*int(grid[i-3][j+3])
            if maxProduct < prod:
                maxProduct = prod

    return maxProduct


def max_antidiagonal_1_product():

    maxProduct = 0

    for j in range(16,-1,-1):

        for i in range(0,j-2,1):

            prod = int(grid[i][j])*int(grid[i+1][j+1])*int(grid[i+2][j+2])*int(grid[i+3][j+3])
            if maxProduct < prod:
                maxProduct = prod

    return maxProduct


def max_antidiagonal_2_product():

    maxProduct = 0

    for j in range(16,4,-1):

        for i in range(19,j-2,-1):

            prod = int(grid[i][j])*int(grid[i-11][j-1])*int(grid[i-2][j-2])*int(grid[i-3][j-3])
            if maxProduct < prod:
                maxProduct = prod

    return maxProduct


print max(max_row_product(),max_column_product(),max_diagonal_1_product(),max_diagonal_2_product(),max_antidiagonal_1_product(),max_antidiagonal_2_product())