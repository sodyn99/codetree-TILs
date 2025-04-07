from collections import deque

S = list(input())
char = ['+', '-', '*']

characters = []
for s in S:
    if s not in char and s not in characters:
        characters.append(s)
# characters.sort()

def calc(arr):
    deq = deque()
    result = 0
    # for a in arr:                 * 먼저 하는 줄 알았네!! 문제좀 똑바로 읽자!!
    #     if deq:
    #         if deq[-1] == '*':
    #             deq.pop()
    #             a *= deq.pop()
    #     deq.append(a)
    curr_char = ''
    for d in arr:
        if d == '-':
            curr_char = '-'
        elif d == '+':
            curr_char = '+'
        elif d == '*':
            curr_char = '*'
        else:
            if curr_char == '-':
                result -= d
            elif curr_char == '*':
                result *= d
            else:
                result += d
    return result

max_result = float('-inf')
tmp_arr = []
def dfs(n):
    global max_result
    global tmp_arr
    arr = []
    if n == len(characters):
        for i in S:
            for j in range(len(characters)):
                if i == characters[j]:
                    arr.append(tmp_arr[j])
            if i in char:
                arr.append(i)
        max_result = max(max_result, calc(arr))
        return
    
    for i in range(1, 5):
        tmp_arr.append(i)
        dfs(n+1)
        tmp_arr.pop()

dfs(0)
print(max_result)