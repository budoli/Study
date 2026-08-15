public class Day002 {
    public static int solution(String s) {
        // TODO: 연속된 같은 문자를 문자 + 개수 형태로 압축했을 때의 길이를 반환하세요.
        // 예: "aaabbc" -> "a3b2c" -> 5

        char[] cha = s.toCharArray();

        int count = 1;
        int answer = 0;

        for (int i=1; i<cha.length; i++) {
            if(cha[i-1] == cha[i]) {
                count++;
            } else {
                answer += compressedLength(count);
                

                count = 1;
            }
        }

        answer += compressedLength(count);

        return answer;
    }

    private static int compressedLength(int count) {
        if (count == 1) {
            return 1;
        }

        return 1 + String.valueOf(count).length();
    }
}

