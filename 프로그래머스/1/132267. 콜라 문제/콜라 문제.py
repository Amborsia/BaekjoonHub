def solution(a, b, n):
    answer = 0
    while n >=a:
        #원래 갯수 - 최대 갯수(n//a)*a + 받은갯수(n//a)*b
        temp = (n//a)
        n = n-(temp*a)+(temp*b)
        answer+=temp*b
    return answer
# exchange_sets = n // a
# new_cola = exchange_sets * b
        
#         # 3. 남은 병의 수 업데이트
#         # (원래 있던 병 - 마트에 준 병) + 새로 받은 병
#         n = (n % a) + new_cola
        
#         # 4. 총 받은 콜라 수 누적
#         answer += new_cola