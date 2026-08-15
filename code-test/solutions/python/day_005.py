def solution(s):
    # TODO: 괄호 문자열이 올바르면 True, 아니면 False를 반환하세요.
    # 예: "([{}])" -> True, "([)]" -> False

    pairs = {
        ')' : '(',
        '}' : '{',
        ']' : '['
    }

    open = {'(','{','['}
    stack = []

    for item in s :
        if item in open :
            stack.append(item)
        elif item in pairs:
            if not stack or stack.pop() != pairs[item] :
                return False



    return not stack

