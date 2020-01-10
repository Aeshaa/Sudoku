def find_empty(arr):
    for row in range(9):
        for col in range(9):
            if (arr[row][col] == 0):
                return (row, col)
    return None



def solve(arr):
    
    find = find_empty(arr)
    if not find:
        return True
    else:
        row, col = find
    
    for num in range(1,10):

        if safe_pos(arr, num, (row, col)):
            arr[row][col] = num

            if(solve(arr)):
                return True

            arr[row][col] = 0

    return False


def safe_pos(arr, num, pos):
    #row

    for i in range (len(arr[0])):
        if arr[pos[0]][i] == num and pos[1] != i:
            return False

    #column
    for i in range(len(arr)):
        if arr[i][pos[1]] == num and pos[0] != i:
            return False

    #box
    row_s = (pos[0] // 3)*3
    col_s = (pos[1] // 3)*3
    for i in range(row_s, row_s+3):
        for j in range(col_s, col_s+3):
            if(arr[i][j] == num) and (i, j) != pos:
                return False

    return True


# def safe_pos(arr, num, pos):
#     return not row_check(arr, row, num) and not col_check(arr, col, num) and not box_check(arr, row, col, num)



# def row_check(arr, row, num):
#     for x in range(9):
#         if(arr[row][x] == num):
#             return True
#     return False


# def col_check(arr, col, num):
#     for x in range(9):
#         if(arr[x][col] == num):
#             return True
#     return False


# def box_check(arr, row, col, num):
#     row_s = (row // 3)*3
#     col_s = (col // 3)*3
#     for i in range(row_s, row_s+3):
#         for j in range(col_s, col_s+3):
#             if(arr[i][j] == num):
#                 return True
#     return False


def print_grid(arr): 
    for i in arr:
        print (i)
        
        
if __name__== "__main__":
    
    #grid=[[0 for x in range(9)]for y in range(9)] 
    
    
    grid = [ [5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9] ]

    if (solve(grid)):
        print_grid(grid)
    else:
        print ('solution does not exist')