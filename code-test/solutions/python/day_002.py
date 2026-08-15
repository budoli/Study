def solution(s):
    # TODO: 연속된 같은 문자를 문자 + 개수 형태로 압축했을 때의 길이를 반환하세요.
    # 예: "aaabbc" -> "a3b2c" -> 5

    s_list = list(s)

    count = 1
    answer = 0

    for i in range(1,len(s_list)) :
        if (s_list[i-1] == s_list[i]) :
            count += 1
        else :
            answer += compressedLength(count)            
            count = 1

    answer += compressedLength(count)

    return answer

def compressedLength(count) :
    if (count == 1) :
        return 1
    
    return 1 + len(str(count))

