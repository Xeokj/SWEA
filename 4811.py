# 4811.py
import sys
input = sys.stdin.readline

usedcol = [0] * 10

def backtr(dpt, sum):
    global N, ans
    if dpt == N:
        if sum < ans:
            ans = sum
        return
    for i in range(N):
        if not usedcol[i] and sum + arr[dpt][i] < ans:
            usedcol[i] = 1
            backtr(dpt + 1, sum + arr[dpt][i])
            usedcol[i] = 0

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 100
    backtr(0, 0)
    print(f'#{tc} {ans}')