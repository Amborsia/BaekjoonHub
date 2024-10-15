import heapq

def solution(scoville, K):
    # 최소 힙으로 변환
    heapq.heapify(scoville)
    mix_count = 0

    while scoville[0] < K:
        # 만약 원소가 하나 남았는데 K 이상이 아니라면, -1을 반환
        if len(scoville) < 2:
            return -1
        
        # 스코빌 지수가 낮은 두 개의 음식 섞기
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        new_scoville = first + (second * 2)
        
        # 새 음식 추가
        heapq.heappush(scoville, new_scoville)
        mix_count += 1

    return mix_count
