def solution(numbers, target):
    # TODO: O(n)으로 풀어보세요.
    # 힌트: dict에 이미 본 숫자와 인덱스를 저장합니다.

    dict = {}

    for z in range(len(numbers)) :
        if(target - numbers[z] in dict) :
            i = dict[target-numbers[z]]
            j = z
            
            break;
            
            
        dict[numbers[z]] = z


    return [i, j]
