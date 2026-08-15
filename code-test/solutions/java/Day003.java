public class Day003 {
    public static int solution(int[] numbers) {
        // TODO: 연속된 하나 이상의 원소를 선택했을 때의 최대 합을 반환하세요.
        // 예: [1, -3, 2, 5, -1] -> 7
        
        int current = numbers[0];
        int answer = numbers[0];

        for(int i=1; i<numbers.length; i++) {
            current = Math.max(current+numbers[i], numbers[i]);
            answer = Math.max(answer, current);
        }
        
        return answer;

    }
}

