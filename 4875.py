# 4875.py
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def BFS(r_st, c_st, N):
    q = list()
    q.append((r_st, c_st))
    visited[r_st][c_st] = 1
    while q:
        curr, curc = q.pop(0)
        #visited[curr][curc] = 0
        for dir in range(4):
            nr = curr + dr[dir]
            nc = curc + dc[dir]
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            if arr[nr][nc] != 1 and visited[nr][nc] == 0:
                if arr[nr][nc] == 3:
                    return 1
                q.append((nr, nc))
                visited[nr][nc] = 1
    return 0

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    for r in range(N):
        nums = input()
        for c in range(N):
            arr[r][c] = int(nums[c])
        for c in range(N):
            if arr[r][c] == 2:
                r_st = r
                c_st = c
    ans = BFS(r_st, c_st, N)
    print(f'#{tc} {ans}')