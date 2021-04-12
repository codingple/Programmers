from collections import defaultdict

def dfs(id,crnt_dict,d,string,res):
    if d == len(id):
        res.append(crnt_dict["-1"])
        return string
    elif id[d] == '*':
        if crnt_dict:
            for k, sub in crnt_dict.items():
                if k != "-1":
                    string+=k
                    dfs(id,sub,d+1,string,res)
                    string = string[:-1]
    elif crnt_dict[id[d]]:
        string+=id[d]
        dfs(id,crnt_dict[id[d]],d+1,string,res)
        string = string[:-1]

def solution(user_id, banned_id):
    answer = 0
    trie = defaultdict(str)
    for j in range(len(user_id)):
        id = user_id[j]
        crnt_dict = trie
        for i in range(len(id)):
            c = id[i]
            if not crnt_dict[c]:
                crnt_dict[c] = defaultdict(str)
            if i == len(id)-1:
                crnt_dict[c]["-1"] = j
            crnt_dict = crnt_dict[c]

    for id in banned_id:
        res = []
        dfs(id, trie, 0, "", res)
        print(res)

    return answer

if __name__ == '__main__':
    print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "abc1**"]))
    print(2)
    print()
    print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["*rodo", "*rodo", "******"]))
    print(2)
    print()
    print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "*rodo", "******", "******"]))
    print(3)