def solution(budgets, M):
    answer = 0
    sm = sum(budgets)
    mx = max(budgets)
    # already meet
    if sm < M :
        return mx;
    # not meet
    mn = min(budgets)
    # set minimum
    if mn * len(budgets) > M :
        mn = 1
    
    while mx - mn != 1:
        sm = 0
        mid = (int) ((mx + mn) / 2)
        for b in budgets:
            sm += mid if b > mid else b
        if sm > M :
            mx = mid
        elif sm < M :
            mn = mid
    
    while sm < M:
        sm = 0
        mid = mid + 1
        for b in budgets:
            sm += mid if b > mid else b
    answer = mid - 1
    return answer