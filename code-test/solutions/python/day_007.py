def solution(k, dungeons):
    # TODO: 현재 피로도로 탐험할 수 있는 던전의 최대 개수를 반환하세요.
    # 예: k = 80, dungeons = [[80, 20], [50, 40], [30, 10]] -> 3

    answer = 0
    visited = [False] * len(dungeons)

    def dfs(k, count) :
        nonlocal answer
        answer = max(answer, count)

        for i in range(0, len(dungeons)) :
            if (visited[i] == False and k>=dungeons[i][0]) :
                visited[i] = True
                dfs(k-dungeons[i][1], count+1)
                visited[i] = False

    dfs(k, 0)

    return answer

