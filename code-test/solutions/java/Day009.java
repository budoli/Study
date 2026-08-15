public class Day009 {
    public static int solution(int[] requests, int budget) {
        // TODO: 배정 총합이 budget 이하가 되는 예산 상한선의 최댓값을 반환하세요.
        // 예: requests = [120, 110, 140, 150], budget = 485 -> 127
        int answer = 0;
        int left = 0;
        int right = 0;

        for (int request : requests) {
            right = Math.max(right, request);
        }

        while (left <= right) {
            int cap = (left + right)/2;
            long total = 0;

            for(int request : requests) {
                total += Math.min(request, cap);
            }
            
            if (total <= budget) {
                answer = cap;
                left = cap + 1;
            } else {
                right = cap -1;
            }
        }
        
        return answer;
    }
}

