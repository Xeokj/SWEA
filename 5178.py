# 5178.py
for tc in range(1, int(input()) + 1):
    N, M, L = map(int, input().split())
    nodes = [0] * (N + 1)

    for i in range(M):
        idx, num = map(int, input().split())
        nodes[idx] = num
    for i in range(N, 0, -1):
        nodes[i//2] += nodes[i]
    print(f'#{tc} {nodes[L]}')