T = int(input())
for tc in range(1, T + 1):
    K, N, M = map(int, input().split())
    stops = list(map(int, input().split()))
    stops.append(N)     # 맨 끝에 N 추가
    diff = stops[:1]    # 충전기 사이의 거리 list
    for i in range(1, M + 1):
        diff.append(stops[i] - stops[i - 1])
    remains = K
    savepoint = -1
    ans = 0
    i = 0
    while i <= M:
        while i <= M and remains - diff[i] >= 0:
            remains -= diff[i]
            i += 1
        if i - savepoint == 1:  # 위의 while 조건을 만족하지 못해서 이동하지 못했을 때
            break
        savepoint = i - 1   # 현재까지 이동 완료한 지점
        remains = K     # remain 초기화
        ans += 1
    if i == M + 1:
        print(f'#{tc} {ans - 1}')   # 시작점에서의 충전 횟수는 포함하지 않으므로 1 차감
    else:
        print(f'#{tc} 0')