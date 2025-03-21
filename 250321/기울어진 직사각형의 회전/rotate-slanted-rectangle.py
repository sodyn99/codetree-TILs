N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
r, c, m1, m2, m3, m4, dir = map(int, input().split())

def rotate(arr, r, c, dir):
    tmp = arr[r][c]
    tmp_r, tmp_c = r, c
    if dir == 0:
        for m in range(m4):
            arr[tmp_r][tmp_c] = arr[tmp_r-1][tmp_c-1]
            tmp_r -= 1
            tmp_c -= 1
        for m in range(m3):
            arr[tmp_r][tmp_c] = arr[tmp_r-1][tmp_c+1]
            tmp_r -= 1
            tmp_c += 1
        for m in range(m2):
            arr[tmp_r][tmp_c] = arr[tmp_r+1][tmp_c+1]
            tmp_r += 1
            tmp_c += 1
        for m in range(m1):
            arr[tmp_r][tmp_c] = arr[tmp_r+1][tmp_c-1]
            tmp_r += 1
            tmp_c -= 1
        arr[r-1][c+1] = tmp
    else:
        for m in range(m1):
            arr[tmp_r][tmp_c] = arr[tmp_r-1][tmp_c+1]
            tmp_r -= 1
            tmp_c += 1
        for m in range(m2):
            arr[tmp_r][tmp_c] = arr[tmp_r-1][tmp_c-1]
            tmp_r -= 1
            tmp_c -= 1
        for m in range(m3):
            arr[tmp_r][tmp_c] = arr[tmp_r+1][tmp_c-1]
            tmp_r += 1
            tmp_c -= 1
        for m in range(m4):
            arr[tmp_r][tmp_c] = arr[tmp_r+1][tmp_c+1]
            tmp_r += 1
            tmp_c += 1
        arr[r-1][c-1] = tmp
    return arr

arr = rotate(arr, r-1, c-1, dir)

for a in arr:
    print(*a)
    