from collections import deque

t_coord = dict({
    1:[0,0], 3:[0,2],
    4:[1,0], 6:[1,2],
    7:[2,0], 9:[2,2],
    2:[0,1],5:[1,1],8:[2,1],0:[3,1]
})

dir = [
    [0,1],[0,-1],[1,0],[-1,0]
]
r = 0
c = 1

def in_range(coord):
    return 0 <= coord[r] and 0 <= coord[c] and coord[r] < 3 and coord[c] < 4

def get_dist(coord,t_coord):
    return abs(coord[r] - t_coord[r]) + abs(coord[c] - t_coord[c])


def solution(numbers, hand):
    answer = ''
    l = [3,0]
    r = [3,2]
    for num in numbers:
        if num == 1 or num == 4 or num == 7:
            answer += 'L'
            l = t_coord[num]
        elif num == 3 or num == 6 or num == 9:
            answer += 'R'
            r = t_coord[num]
        else:
            t= t_coord[num]
            l_dist = get_dist(l,t_coord[num])
            r_dist = get_dist(r,t_coord[num])
            if l_dist < r_dist or (l_dist == r_dist and hand == "left"):
                answer += 'L'
                l = t_coord[num]
            elif r_dist < l_dist or (l_dist == r_dist and hand == "right"):
                answer += 'R'
                r = t_coord[num]

    return answer

if __name__ == '__main__':
    print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],"left"))
    print("LRLLRRLLLRR")