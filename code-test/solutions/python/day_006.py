from collections import deque

def solution(priorities, location):
    # TODO: location 위치의 문서가 몇 번째로 출력되는지 반환하세요.
    # 예: priorities = [2, 1, 3, 2], location = 2 -> 1

    queue = deque()
    answer = 0

    for i in range(0, len(priorities)) :
        queue.append([priorities[i], i])

    while (queue) :
        current = queue.popleft()
        currentPriorities = current[0]
        currentIndex = current[1]

        big = False

        for item in queue :
            if (item[0] > currentPriorities) :
                big = True
                break

        if (big) :
            queue.append(current)
        else :
            answer+=1
            if (location == currentIndex):
                return answer


    return answer

