import java.util.*;

public class Day005 {
    public static boolean solution(String s) {
        // TODO: 괄호 문자열이 올바르면 true, 아니면 false를 반환하세요.
        // 예: "([{}])" -> true, "([)]" -> false
        Map<Character, Character> pairs = new HashMap<>();
        pairs.put(')','(');
        pairs.put('}','{');
        pairs.put(']','[');

        Set<Character> open = new HashSet<>();
        open.add('(');
        open.add('{');
        open.add('[');

        char[] cha = s.toCharArray();
        Stack<Character> stack = new Stack<>();

        for(char item : cha) {
            if(open.contains(item)) {
                stack.push(item);
            } else {
                if (stack.isEmpty() || stack.pop() != pairs.get(item)) {
                    return false;
                }
            }
        }

        return stack.isEmpty();
    }
}

