# 1226.py
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def DFS(curr, curc):
    global ans
    if arr[curr][curc] == 3:
        ans = 1
        return
    for dir in range(4):
        nr = curr + dr[dir]
        nc = curc + dc[dir]
        if nr < 0 or nr >= 16 or nc < 0 or nc >= 16:
            continue
        if arr[nr][nc] != 1 and visited[nr][nc] == 0:
            visited[nr][nc] = 1
            DFS(nr, nc)
            visited[nr][nc] = 0

for _ in range(10):
    tc = int(input())
    ans = 0
    arr = [[0] * 16 for _ in range(16)]
    visited = [[0] * 16 for _ in range(16)]
    for r in range(16):
        nums = int(input())
        arr[r] = list(map(int, str(nums)))
        for c in range(16):
            if arr[r][c] == 2:
                r_st = r
                c_st = c
    visited[r_st][c_st] = 1
    DFS(r_st, c_st)
    print(f'#{tc} {ans}')