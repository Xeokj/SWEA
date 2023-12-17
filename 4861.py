# 4861.py
def check():
    global N, M, arr
    for i in range(N):
        for j in range(N - M + 1):
            tmp = ""
            # 부분 문자열 추출
            for k in range(M):
                tmp += arr[i][j + k]
            # tmp와 tmp를 뒤집은 게 같다면 tmp를 return
            if tmp == tmp[::-1]:
                return tmp
    # 회문이 없을 때 그냥 return
    return

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input().strip() for _ in range(N)]
    ans = check()
    if ans: # return한 문자열이 있을 때
        print(f'#{tc} {ans}')
        continue
    else:
        # arr를 전치시킴
        arr = list(zip(*arr[::-1]))
        ans = check()
        print(f'#{tc} {ans}')