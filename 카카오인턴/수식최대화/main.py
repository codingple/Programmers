from collections import deque
from itertools import permutations
import copy

oper = ['-', '*', '+']

def operation(one,two,oper):
    if oper == '-':
        return one-two
    elif oper == '*':
        return one*two
    elif oper == '+':
        return one+two

def solution(expression):
    answer = 0
    operand = deque()
    operator = deque()

    idx = 0
    for i in range(len(expression)):
        c = expression[i]
        if c in oper:
            operand.append(int(expression[idx:i]))
            operator.append(c)
            idx = i+1
    operand.append(int(expression[idx:]))

    orders = set(permutations(oper,3))

    for order in orders:
        crnt_operator = copy.deepcopy(operator)
        crnt_operand = copy.deepcopy(operand)
        for crnt_op in order:
            one = crnt_operand.popleft()
            for _ in range(len(crnt_operator)):
                two = crnt_operand.popleft()
                op = crnt_operator.popleft()

                if op == crnt_op:
                    one = operation(one,two,op)
                else:
                    crnt_operand.append(one)
                    crnt_operator.append(op)
                    one = two
            crnt_operand.append(one)
        answer = max(abs(crnt_operand.pop()),answer)

    return answer

if __name__ == '__main__':
    print(solution("100-200*300-500+20"))
    print(60420)
    print(solution("50*6-3*2"))
    print(300)