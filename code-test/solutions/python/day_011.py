def solution(n, edges):
    # TODO: 무방향 그래프의 연결 요소 개수를 반환하세요.
    # 예: n = 5, edges = [[1, 2], [2, 3], [4, 5]] -> 2
    graph = [[] for _ in range(n + 1)]

    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * (n + 1)
    answer = 0

    def dfs(node):
        visited[node] = True

        for next in graph[node]:
            if not visited[next]:
                dfs(next)

    for node in range(1, n + 1):
        if not visited[node]:
            answer += 1
            dfs(node)

    return answer
