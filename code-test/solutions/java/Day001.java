import java.util.*;

public class Day001 {
    public static int[] solution(int[] numbers, int target) {
        // TODO: O(n)으로 풀어보세요.
        // 힌트: HashMap에 이미 본 숫자와 인덱스를 저장합니다.

        HashMap<Integer, Integer> hm = new HashMap<>();
        int i = 0;
        int j = 0;
        for (int z=0; z<numbers.length; z++) {
            if(hm.containsKey(target - numbers[z])) {
                i = hm.get(target - numbers[z]);
                j = z;

                break;
            } else {
                hm.put(numbers[z], z);
            }

        }
        
        return new int[] {i, j};
    }
}
