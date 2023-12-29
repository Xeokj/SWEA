# 5174.py
def search(node):
    global ans
    if node > 0:
        ans += 1
        search(left[node])
        search(right[node])

for tc in range(1, int(input()) + 1):
    E, N = map(int, input().split())
    edges = list(map(int, input().split()))
    left = [0] * (E + 2)
    right = [0] * (E + 2)

    for i in range(E):
        p, c = edges[i * 2], edges[i * 2 + 1]
        if not left[p]:
            left[p] = c
        else:
            right[p] = c
    ans = 0
    search(N)
    print(f'#{tc} {ans}')