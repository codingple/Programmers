import sys
sys.setrecursionlimit(10 ** 10)

board = []
check = []
before_after = []

def dfs(s):
    for d in board[s]:
        if check[d]:
            check[d] = 0
            if before_after[d] >= -1:
                if before_after[d] > -1:
                    release = before_after[d]
                    before_after[release] = -1
                    before_after[d] = -1
                    if not check[release]:
                        dfs(release)
                dfs(d)

def solution(n, path, order):
    global board, check, before_after
    board = [[] for _ in range(n)]
    check = [1 for _ in range(n)]
    before_after = [-1 for _ in range(n)]

    for _from, _to in path:
        board[_from].append(_to)
        board[_to].append(_from)

    for before, after in order:
        before_after[before] = after
        before_after[after] = -2

    check[0] = 0
    dfs(0)
    if  sum(check) == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    print(solution(9,[[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[1,2],[2,1]]))