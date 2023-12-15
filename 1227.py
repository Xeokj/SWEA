# 1227.py
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def BFS(r_st, c_st):
    q = list()
    q.append((r_st, c_st))
    visited[r_st][c_st] = 1
    while q:
        curr, curc = q.pop(0)
        #visited[curr][curc] = 0
        for dir in range(4):
            nr = curr + dr[dir]
            nc = curc + dc[dir]
            if nr < 0 or nr >= 100 or nc < 0 or nc >= 100:
                continue
            if arr[nr][nc] != 1 and visited[nr][nc] == 0:
                if arr[nr][nc] == 3:
                    return 1
                q.append((nr, nc))
                visited[nr][nc] = 1
    return 0

for _ in range(10):
    tc = int(input())
    arr = [[0] * 100 for _ in range(100)]
    visited = [[0] * 100 for _ in range(100)]
    for r in range(100):
        nums = int(input())
        arr[r] = list(map(int, str(nums)))
        for c in range(100):
            if arr[r][c] == 2:
                r_st = r
                c_st = c
    ans = BFS(r_st, c_st)
    print(f'#{tc} {ans}')