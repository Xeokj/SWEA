T = int(input())
for tc in range(1,T+1):
    ans = 0
    N, M = map(int, input().split())
    # (N+1)*(N*1) 크기의 배열 만들기
    arr = [[0 for _ in range(N+1)] for _ in range(N+1)]
    # (1,1) 인덱스부터 입력 받기
    for i in range(1,N+1):
        temp = input().split()
        for j in range(1,N+1):
            arr[i][j] = int(temp[j-1])
    # 누적합 구하기
    for i in range(1,N+1):
        for j in range(1,N+1):
                arr[i][j] += (arr[i-1][j] + arr[i][j-1] - arr[i-1][j-1])
    ans = 0
    for i in range(M,N+1):
        for j in range(M,N+1):
            sum = arr[i][j] - arr[i-M][j] - arr[i][j-M] + arr[i-M][j-M]
            if sum > ans: ans = sum # 최댓값 갱신
    print(f'#{tc} {ans}')