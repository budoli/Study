import java.util.*;

public class Day011 {
        static List<List<Integer>> graph;
        static boolean[] visited;

    public static int solution(int n, int[][] edges) {
        // TODO: 무방향 그래프의 연결 요소 개수를 반환하세요.
        // 예: n = 5, edges = [[1, 2], [2, 3], [4, 5]] -> 2
        graph = new ArrayList<>();
        visited = new boolean[n + 1];
        int answer = 0;

        for(int i=0; i<=n; i++) {
            graph.add(new ArrayList<>());
        }

        for(int[] edge: edges) {
            int a = edge[0];
            int b = edge[1];
        
            graph.get(a).add(b);
            graph.get(b).add(a);
        }

        for (int i=1; i<= n; i++) {
            if (!visited[i]) {
                answer += 1;
                dfs(i);
            }
        }



        return answer;
    }
    
    static void dfs(int node) {
        visited[node] = true;

        for (int next : graph.get(node)) {
            if (! visited[next]) {
                dfs(next);
            }
        }
    }
}

