dy = [0,1,0,-1]
dx = [1,0,-1,0]

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())

    # (N+1)*(N*1) 크기의 배열 만들기
    arr = [[0 for _ in range(M+2)] for _ in range(N+2)]

    # (1,1) 인덱스부터 입력 받기
    for i in range(1,N+1):
        temp = input().split()
        for j in range(1,M+1):
            arr[i][j] = int(temp[j-1])

    ans = 0
    for i in range(1,N+1):
        for j in range(1,M+1):
            sum = arr[i][j]
            for dir in range(4):
                ny = i + dy[dir]
                nx = j + dx[dir]
                sum += arr[ny][nx]
            if sum > ans: ans = sum
    print(f'#{tc} {ans}')