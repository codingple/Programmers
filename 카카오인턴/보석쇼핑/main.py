from collections import defaultdict

def solution(gems):
    answer = []
    shortest = 100000
    num_list = defaultdict(int)
    for word in gems:
        num_list[word] = 0
    N = len(gems)
    count_zero = len(num_list)

    l = r = 0

    while r < N:
        while count_zero != 0 and r < N:
            num_list[gems[r]] += 1
            if num_list[gems[r]] == 1:
                count_zero -= 1
            r+=1

        if r != N:
            while l < N:
                num_list[gems[l]] -= 1
                if num_list[gems[l]] == 0:
                    count_zero += 1
                    l += 1
                    break
                l+=1
        else:
            while count_zero == 0 and l < N:
                num_list[gems[l]] -= 1
                if num_list[gems[l]] == 0:
                    count_zero+=1
                l+=1

        if r - l + 1 < shortest:
            shortest = r - l + 1
            answer = [l,r]


    return answer

if __name__ == '__main__':
    print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
    print([3, 7])
    print()
    print(solution(["AA", "AB", "AC", "AA", "AC"]))
    print([1, 3])
    print()
    print(solution(["XYZ", "XYZ", "XYZ"]))
    print([1, 1])
    print()
    print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
    print([1, 5])