board= [[0,0,1,0,7,0,0,0,9],
        [6,0,9,8,3,1,7,5,0],
        [8,0,7,0,0,9,0,0,6],
        [0,0,4,9,0,0,1,0,0],
        [0,8,0,0,6,3,0,0,0],
        [0,0,0,4,1,0,0,7,3],
        [0,0,0,1,0,7,2,3,0],
        [2,1,0,3,9,0,5,0,0],
        [0,5,3,2,0,4,6,0,0]]

def printboard(bo):
    for i in range(9):
        if (i)%3 == 0 and i !=0:
            print("----------------------")

        for j in range(9):
            if (j)%3==0 and j !=0: 
                print("|", end=' ')
            print(bo[i][j],end=' ')
        print()

def position(bo):
    for i in range(9):
        for j in range(9):
            if bo[i][j] == 0:
                return i,j
            
    return False

def valid(bo,pos,value):
    if value in bo[pos[0]]:
        return False

    for i in range(9):
        if value == bo[i][pos[1]]:
            return False

    for i in range((pos[0]//3)*3,((pos[0]//3)*3)+3):
        for j in range((pos[1]//3)*3,((pos[1]//3)*3)+3):
            if value == bo[i][j]:
                return False
    return True

def solve(bo):
    
    empty_position = position(bo)
    if not empty_position:
        return True
    else:
        i,j = empty_position

    for v in range(1,10):
        if valid(bo,empty_position,v):
            bo[i][j]=v
            if solve(bo):
                return True
            bo[i][j]=0
    return False                





printboard(board)
solve(board)
print("solving.")
print("solving..")
print("solving...")
print("solved")
printboard(board)

# output =
'''

5 3 1 | 6 7 2 | 4 8 9
6 4 9 | 8 3 1 | 7 5 2
8 2 7 | 5 4 9 | 3 1 6
----------------------
3 7 4 | 9 2 8 | 1 6 5 
1 8 5 | 7 6 3 | 9 2 4
9 6 2 | 4 1 5 | 8 7 3
----------------------
4 9 6 | 1 5 7 | 2 3 8
2 1 8 | 3 9 6 | 5 4 7
7 5 3 | 2 8 4 | 6 9 1 

'''
