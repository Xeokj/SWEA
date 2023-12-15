# 5105.py
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs():
    q = []
    q.append((st_r, st_c))
    maze[st_r][st_c] = -1
    while q:
        cur_r, cur_c = q.pop(0)
        for dir in range(4):
            nr = cur_r + dr[dir]
            nc = cur_c + dc[dir]
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            if maze[nr][nc] == 0:
                q.append((nr, nc))
                maze[nr][nc] = maze[cur_r][cur_c] - 1
            elif maze[nr][nc] == 3:
                maze[nr][nc] = abs(maze[cur_r][cur_c]) - 1
                return

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    ans = 0
    maze = [list(map(int, input())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                st_r = i
                st_c = j
            elif maze[i][j] == 3:
                end_r = i
                end_c = j
    bfs()
    if maze[end_r][end_c] == 3:
        maze[end_r][end_c] = 0
    print(f'#{tc} {maze[end_r][end_c]}')