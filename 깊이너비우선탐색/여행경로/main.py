import sys
sys.setrecursionlimit(100000)

def dfs(board, answer, start, n):
    if n == len(answer):
        return True

    if board.get(start):
        for i in range(len(board[start])):
            _to = board[start][i]
            del board[start][i]
            answer.append(_to)
            if dfs(board,answer,_to, n):
                return True
            board[start].insert(i,_to)
            answer.pop()

    return False

def solution(tickets):
    answer = ["ICN"]
    board = dict()
    tickets.sort(key=lambda x:(x[0],x[1]))
    for _from, _to in tickets:
        if board.get(_from):
            board[_from].append(_to)
        else:
            board[_from] = [_to]
    dfs(board, answer, "ICN", len(tickets)+1)
    return answer

if __name__ == '__main__':
    print(solution([['ICN','A'],['A','B'],['A','C'],['C','A'],['B','D']]))