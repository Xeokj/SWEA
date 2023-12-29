# 1953.py
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def avail(cur, dest, dir):
    if cur == 1:
        if dir == 0 and (dest == 1 or dest == 2 or dest == 5 or dest == 6):
            return 1
        elif dir == 1 and (dest == 1 or dest == 2 or dest == 4 or dest == 7):
            return 1
        elif dir == 2 and (dest == 1 or dest == 3 or dest == 4 or dest == 5):
            return 1
        elif dir == 3 and (dest == 1 or dest == 3 or dest == 6 or dest == 7):
            return 1
    elif cur == 2:
        if dir == 0 and (dest == 1 or dest == 2 or dest == 5 or dest == 6):
            return 1
        elif dir == 1 and (dest == 1 or dest == 2 or dest == 4 or dest == 7):
            return 1
    elif cur == 3:
        if dir == 2 and (dest == 1 or dest == 3 or dest == 4 or dest == 5):
            return 1
        elif dir == 3 and (dest == 1 or dest == 3 or dest == 6 or dest == 7):
            return 1
    elif cur == 4:
        if dir == 0 and (dest == 1 or dest == 2 or dest == 5 or dest == 6):
            return 1
        elif dir == 3 and (dest == 1 or dest == 3 or dest == 6 or dest == 7):
            return 1
    elif cur == 5:
        if dir == 1 and (dest == 1 or dest == 2 or dest == 4 or dest == 7):
            return 1
        elif dir == 3 and (dest == 1 or dest == 3 or dest == 6 or dest == 7):
            return 1
    elif cur == 6:
        if dir == 1 and (dest == 1 or dest == 2 or dest == 4 or dest == 7):
            return 1
        elif dir == 2 and (dest == 1 or dest == 3 or dest == 4 or dest == 5):
            return 1
    elif cur == 7:
        if dir == 0 and (dest == 1 or dest == 2 or dest == 5 or dest == 6):
            return 1
        elif dir == 2 and (dest == 1 or dest == 3 or dest == 4 or dest == 5):
            return 1
    return 0

for tc in range(1, int(input()) + 1):
    N, M, R, C, L = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    q = deque()
    q.append((R, C, 1))
    visited[R][C] = 1
    ans = 1
    while q:
        cr, cc, t = q.popleft()
        cd = board[cr][cc]
        if t == L:
            break
        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            if visited[nr][nc] == 0 and board[nr][nc] != 0 and avail(board[cr][cc], board[nr][nc], d):
                visited[nr][nc] = 1
                q.append((nr, nc, t + 1))
                ans += 1
    print(f'#{tc} {ans}')