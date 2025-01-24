a, b = map(int, input().split())

# Write your code here!
def cal(a, b):
    if a > b:
        return 2 * a, b + 10
    else:
        return a + 10, 2 * b

A, B = cal(a, b)
print(A, B)