from collections import deque

def solution(board, moves):
    answer = 0
    basket = deque()
    column = []

    for j in range(len(board)):
        column.append(deque())
        for i in range(len(board)):
            if board[i][j] != 0:
                column[j].append(board[i][j])

    for c in moves:
        c -= 1
        if len(column[c]):
            basket.append(column[c].popleft())
            if len(basket) >= 2 and basket[-1] == basket[-2]:
                answer +=2
                basket.pop()
                basket.pop()

    return answer

if __name__ == '__main__':
    print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))
    print(4)