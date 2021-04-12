def solution(s):
    answer = []
    idx = [[] for _ in range(10 ** 5 + 1)]
    cnt = [0 for _ in range(10 ** 5 + 1)]
    l = r = 0
    for i in range(len(s)):
        c = s[i]
        if l <= r and ord('1') <= ord(c) and ord(c) <= ord('9'):
            l = i
        elif r <= l and c == '}':
            r = i
            union = list(map(int,s[l:r].split(',')))
            for num in union:
                cnt[num] += 1
                idx[cnt[num]].append(num)
                if cnt[num] != 1:
                    idx[cnt[num]-1].remove(num)
    for i in range(len(idx)-1,0,-1):
        if len(idx[i]) != 0:
            answer.append(idx[i][0])
    return answer

if __name__ == '__main__':
    print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
    print([2, 1, 3, 4])
    print()

    print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
    print([2, 1, 3, 4])
    print()

    print(solution("{{20,111},{111}}"))
    print([111, 20])
    print()

    print(solution("{{123}}"))
    print([123])
    print()

    print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
    print([3, 2, 4, 1])