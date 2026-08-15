def solution(meetings):
    # TODO: 한 회의실에서 겹치지 않게 진행할 수 있는 회의의 최대 개수를 반환하세요.
    # 예: [[1, 4], [2, 3], [3, 5], [4, 6]] -> 2

    meetings.sort(key=lambda x: (x[1], x[0]))

    lastend = 0
    answer = 0
    
    for i in range(0, len(meetings)) :
        if(meetings[i][0] >= lastend) :
            answer+=1
            lastend=meetings[i][1]

    return answer

