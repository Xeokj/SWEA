def horz():
# 가로
    for i in range(9):
        cnt = [0 for x in range(10)]
        for j in range(9):
            num = sudoku[i][j]
            if cnt[num]:
                return 0
            cnt[num] = 1
    return 1

def vert():
# 세로
    for j in range(9):
        cnt = [0 for x in range(10)]
        for i in range(9):
            num = sudoku[i][j]
            if cnt[num]:
                return 0
            cnt[num] = 1
    return 1

def inbox():
# 박스
    for y in range(3):
        for x in range(3):
            cnt = [0 for k in range(10)]
            for i in range(y*3,y*3+3):
                for j in range(x*3,x*3+3):
                    num = sudoku[i][j]
                    if cnt[num]:
                        return 0
                    cnt[num] = 1
    return 1

T = int(input())

for tc in range(1, T + 1):
    sudoku = [0 for _ in range(9)]
    for i in range(9):
        sudoku[i] = list(map(int, input().split()))
    # 가로 확인
    chk = horz()
    # 세로 확인
    if chk == 1:
        chk = vert()
    # 박스 확인
    if chk == 1:
        chk = inbox()
    print(f'#{tc} {chk}')