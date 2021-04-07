from collections import deque

dir = [
    [0,1],[0,-1],[1,0],[-1,0]
]
r,c = 0, 1
N = 0
max_cost = 0

def in_range(coord):
    global N
    return 0<=coord[r] and 0<=coord[c] and coord[r]<N and coord[c]<N

def bfs(board,check,coord,cost,crnt_d):
    global max_cost
    min_cost = max_cost

    q = deque()
    q.append([coord,cost,crnt_d])

    while len(q):
        crnt = q.popleft()
        coord = crnt[0]
        cost = crnt[1]
        crnt_d = crnt[2]

        if coord[r] == N-1 and coord[c] == N-1:
            min_cost = min(min_cost,cost)

        for d in range(4):
            nw_coord = [coord[r]+dir[d][r],coord[c]+dir[d][c]]
            if in_range(nw_coord) and board[nw_coord[r]][nw_coord[c]] == 0:
                if crnt_d == 5:
                    check[nw_coord[r]][nw_coord[c]] = cost+100
                    q.append([nw_coord,cost+100,d])
                elif crnt_d == d and cost+100 <= check[nw_coord[r]][nw_coord[c]]:
                    check[nw_coord[r]][nw_coord[c]] = cost+100
                    q.append([nw_coord,cost+100,d])
                elif cost+600 <= check[nw_coord[r]][nw_coord[c]]:
                    check[nw_coord[r]][nw_coord[c]] = cost+600
                    q.append([nw_coord,cost+600,d])

    return min_cost



def solution(board):
    global max_cost, N
    N = len(board)
    max_cost = N * N * 600
    check = [[max_cost for _ in range(N)] for __ in range(N)]
    check[0][0] = 0
    check[0][0] = 0


    return bfs(board,check,[0,0],0,5)

if __name__ == '__main__':
    print(solution([[0,0,0],[0,0,0],[0,0,0]]))
    print(900)
    print()

    print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
    print(3800)
    print()

    print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))
    print(2100)
    print()

    print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))
    print(3200)