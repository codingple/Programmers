def solution(n, results):
    answer = 0
    win = [set() for __ in range(n+1)]
    lose = [set() for __ in range(n+1)]

    for i in range(1, n+1):
        for data in results:
            winner = data[0]
            loser = data[1]
            if i == winner:
                win[winner].add(loser)
            if i == loser:
                lose[loser].add(winner)

        for node in lose[i]:
            win[node].update(win[i])
        for node in win[i]:
            lose[node].update(lose[i])

    for i in range(1,n+1):
        if len(win[i]) + len(lose[i]) == n - 1:
            answer += 1

    return answer

if __name__ == '__main__':
    print(solution(7, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5], [5,6], [6,7]]), 4)