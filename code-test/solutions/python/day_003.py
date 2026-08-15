def solution(numbers):
    # TODO: 연속된 하나 이상의 원소를 선택했을 때의 최대 합을 반환하세요.
    # 예: [1, -3, 2, 5, -1] -> 7
    
    current=numbers[0]
    answer=numbers[0]

    for i in range(1, len(numbers)) :
        current= max(current+numbers[i], numbers[i])
        answer= max(current, answer)

    return answer

