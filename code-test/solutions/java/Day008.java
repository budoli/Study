public class Day008 {
    public static int solution(int[] numbers, int k) {
        // TODO: 합이 k가 되는 연속 구간의 개수를 반환하세요.
        // 예: numbers = [1, 2, 1, 3, 2], k = 3 -> 3

        int answer = 0;
        int left = 0;
        int sum = 0;

        for (int right = 0; right< numbers.length; right++) {
            sum += numbers[right];
            
            while(sum > k) {
                sum -= numbers[left];
                left++;
            }
            if (sum == k) {
                answer++;
            }
        }

        return answer;
    }
}

