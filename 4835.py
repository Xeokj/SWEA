T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    sum = nums[:]
    for i in range(1, N):
        sum[i] += sum[i - 1]
    min = sum[M - 1]
    max = sum[M - 1]
    for i in range(M, N):
        if (sum[i] - sum[i - M])> max:
            max = sum[i] - sum[i - M]
        elif (sum[i] - sum[i - M]) < min:
            min = sum[i] - sum[i - M]
    print(f'#{tc} {max - min}')