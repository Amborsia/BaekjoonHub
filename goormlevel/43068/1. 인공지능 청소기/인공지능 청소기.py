# case 설정
case = int(input())

# 좌표 및 횟수 초기값 설정
lit = [list(map(int,input().split())) for _ in range(case)]
    

for i in range(case):
    # 최소 움직임 제약
    if abs(lit[i][0]) + abs(lit[i][1]) > lit[i][2]:
        print('NO')

    # 도달 할 수 있는지 여부 판단(odd, even 판단)
    elif (abs(lit[i][0]) + abs(lit[i][1])) % 2 == lit[i][2] % 2:
        print('YES')
        
    else: 
        print('NO')