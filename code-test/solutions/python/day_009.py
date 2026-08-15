def solution(requests, budget):
    # TODO: 배정 총합이 budget 이하가 되는 예산 상한선의 최댓값을 반환하세요.
    # 예: requests = [120, 110, 140, 150], budget = 485 -> 127
    answer = 0
    left = 0
    right = max(requests)

    while left <= right:
        cap = (left + right) // 2
        total = 0

        for request in requests:
            total += min(request, cap)

        if total <= budget:
            answer = cap
            left = cap + 1
        else:
            right = cap - 1

    return answer
