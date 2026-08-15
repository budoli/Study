import java.util.*;

public class Day004 {
    public static int solution(int[][] meetings) {
        // TODO: 한 회의실에서 겹치지 않게 진행할 수 있는 회의의 최대 개수를 반환하세요.
        // 예: [[1, 4], [2, 3], [3, 5], [4, 6]] -> 2

        Arrays.sort(meetings, (a,b) -> {
            if(a[1] == b[1]) {
                return a[0] - b[0];
            }
            return a[1] - b[1];
        });

        int lastend = 0;
        int answer = 0;

        for(int i=0; i<meetings.length; i++){
            if (meetings[i][0] >= lastend) {
                answer++;
                lastend = meetings[i][1];
            }
        }

        return answer;
    }
}

