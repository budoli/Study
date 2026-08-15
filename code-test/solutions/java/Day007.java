public class Day007 {
    staitc int answer = 0;
    static void dfs(int k, int[][] dungeons, int count, boolean[] visited) {
        answer = Math.max(answer, count);
        
        for (int i=0; i< dungeons.length; i++) {
            if (visited[i] == false && k>=dungeons[i][0]) {
                visited[i] = true;
                dfs(k-dungeons[i][1], dungeons, count+1, visited);
                visited[i] = false;
            }
        }

    }

    public static int solution(int k, int[][] dungeons) {
        // TODO: 현재 피로도로 탐험할 수 있는 던전의 최대 개수를 반환하세요.
        // 예: k = 80, dungeons = [[80, 20], [50, 40], [30, 10]] -> 3
        int answer = 0;
        boolean[] visited = new boolean[dungeons.length];

        dfs(k,dungeons, 0, visited);

        return answer;
    }
}

