def solution(clothes):
    # TODO: 서로 다른 의상 조합의 개수를 반환하세요.
    # 예: [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]] -> 5
    answer = 1
    counts = {}
    for name, type in clothes:
        counts[type] = counts.get(type, 0) + 1

    for count in counts.values():
        answer *= count + 1

    answer -= 1
    return answer
