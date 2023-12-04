# 1859.py
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    values = list(map(int, input().split()))
    ans = 0
    Max = values[N - 1]
    for i in reversed(range(N)):
        if(values[i] > Max):
            Max = values[i]
        else:
            ans += (Max - values[i])
    print(f'#{t} {ans}')
