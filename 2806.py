# 2806.py
import sys
input = sys.stdin.readline

def backtr(row):
    global N, ans
    if row == N:
        ans += 1
        return
    for col in range(N):
        if not usedcol[col] and not ldiag[row + col]:
            Min = min(row, col)
            if col - Min == 0 and not rdiag[(row - Min) * 2]:
                usedcol[col] = 1
                ldiag[row + col] = 1
                rdiag[(row - Min) * 2] = 1
                backtr(row + 1)
                usedcol[col] = 0
                ldiag[row + col] = 0
                rdiag[(row - Min) * 2] = 0
            elif col - Min != 0 and not rdiag[(col - Min) * 2 - 1]:
                usedcol[col] = 1
                ldiag[row + col] = 1
                rdiag[(col - Min) * 2 - 1] = 1
                backtr(row + 1)
                usedcol[col] = 0
                ldiag[row + col] = 0
                rdiag[(col - Min) * 2 - 1] = 0

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    usedcol = [0] * N
    ldiag = [0] * (2 * N - 1)
    rdiag = [0] * (2 * N - 1)
    ans = 0
    backtr(0)
    print(f'#{tc} {ans}')