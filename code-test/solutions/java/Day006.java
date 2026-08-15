import java.util.*;

public class Day006 {
    public static int solution(int[] priorities, int location) {
        // TODO: location 위치의 문서가 몇 번째로 출력되는지 반환하세요.
        // 예: priorities = [2, 1, 3, 2], location = 2 -> 1
        
        Queue<int[]> queue = new LinkedList<>();
        int answer = 0;

        for(int i=0; i<priorities.length; i++) {
            queue.offer(new int[]{priorities[i], i});
        }
        
        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int currentPriorities = current[0];
            int currentIndex = current[1];

            boolean big = false;

            for(int[] item : queue) {
                if (item[0] > currentPriorities) {
                    big = true;
                    break;
                }
            }

            if(big) {
                queue.offer(current);
            } else {
                answer++;

                if (currentIndex == location) {
                    return answer;
                }
            }
        }



        return answer;
    }
}

