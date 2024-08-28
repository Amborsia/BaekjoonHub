# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

# 입력 받기
groom, baram = map(int, input().split())
D = int(input())

# D번째 밤까지 반복
for i in range(D):
    if i % 2 == 0:  # 구름이의 차례
        transfer = (groom + 1) // 2  # 반올림 처리
        groom -= transfer
        baram += transfer
    else:  # 바람이의 차례
        transfer = (baram + 1) // 2  # 반올림 처리
        baram -= transfer
        groom += transfer

# 결과 출력
print(f"{groom} {baram}")
