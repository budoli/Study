def solution(numbers, k):
    # TODO: 합이 k가 되는 연속 구간의 개수를 반환하세요.
    # 예: numbers = [1, 2, 1, 3, 2], k = 3 -> 3

    # index 0번을 left, 1번에 right, sum을 설정
    # for () {
    # if sum == k answer++
    # else right를 한칸 오른쪽으로 밀고 다시 비교
    # if sum > k left를 증가시키고 증가 전 값을 제외

    answer = 0
    left = 0
    sum = 0

    for right in range(0, len(numbers)):
        sum += numbers[right]
        while sum > k:
            sum -= numbers[left]
            left += 1
        if sum == k:
            answer += 1

    return answer
