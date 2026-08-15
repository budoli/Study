import java.util.*;

public class Day010 {
    public static int solution(String[][] clothes) {
        // TODO: 서로 다른 의상 조합의 개수를 반환하세요.
        // 예: [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]] -> 5
        
        int answer = 1;
        Map<String, Integer> counts = new HashMap<>();

        for (String[] cloth : clothes) {
            String type = cloth[1];
            counts.put(type, counts.getOrDefault(type, 0) + 1);
        }

        for (int count : counts.values()) {
        answer *= count + 1;
        }

        return answer - 1;
    }
}

