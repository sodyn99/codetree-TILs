a, b = map(int, input().split())

# Write your code here!
def cal(a, b):
    return min(a, b) + 10, 2 * max(a, b)

A, B = cal(a, b)
print(A, B)