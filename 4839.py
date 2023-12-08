def bs(l, r, tg, cnt):
    global t
    if (l+r)//2 < tg:
        bs((l+r)//2, r, tg, cnt+1)
    elif (l+r)//2 > tg:
        bs(l, (l+r)//2, tg, cnt+1)
    else:
        t = cnt

T = int(input())
for tc in range(1,T+1):
    P, Pa, Pb = map(int, input().split())
    bs(1, P, Pa, 1)
    A = t
    bs(1, P, Pb, 1)
    B = t
    print(f'#{tc}', end=' ')
    if A < B: print('A')
    elif A > B: print('B')
    else: print(0)