# 1247.py
import sys
input = sys.stdin.readline

def backtr(dpt, y, x, dist):
    global N, ans
    if dpt == N:
        global eny, enx
        if dist + abs(y - eny) + abs(x - enx) < ans:
            ans = dist + abs(y - eny) + abs(x - enx)
        return
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            backtr(dpt + 1, arr[i * 2], arr[i * 2 + 1], dist + abs(y - arr[i * 2]) + abs(x - arr[i * 2 + 1]))
            visited[i] = 0

for tc in range(1, int(input()) + 1):
    N = int(input())
    ans = 2200
    arr = list(map(int, input().split()))
    sty, stx, eny, enx = arr[0], arr[1], arr[2], arr[3]
    for _ in range(4):
        arr.pop(0)
    visited = [0] * N
    backtr(0, sty, stx,0)
    print(f'#{tc} {ans}')