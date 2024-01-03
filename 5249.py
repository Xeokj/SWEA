# 5249.py
import heapq

def Prim():
    dist = [987654321] * (V + 1)
    visited = [0] * (V + 1)
    mheap = []
    # 0번 노드를 기준으로 연결된 노드들 mheap에 push
    heapq.heappush(mheap, (0, 0))
    dist[0] = 0
    while mheap:
        # minimum heap에서 w가 가장 작은 것 pop함 (new weight, new vertex)
        cw, cv = heapq.heappop(mheap)
        visited[cv] = 1
        for x in g[cv]:
            nw, nv = map(int, x)
            if not visited[nv] and nw < dist[nv]:
                heapq.heappush(mheap, x)
                dist[nv] = nw
    return sum(dist)

for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    g = [[] for _ in range(V + 1)]
    for _ in range(E):
        st, en, w = map(int, input().split())
        g[st].append((w, en))
        g[en].append((w, st))
    print(f'#{tc} {Prim()}')