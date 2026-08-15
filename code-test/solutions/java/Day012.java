public class Day012 {
    public static int solution(int[][] grid) {
        // TODO: (0, 0)에서 오른쪽 아래 칸까지의 최단 거리를 반환하세요.
        // 도착할 수 없으면 -1을 반환하세요.
        int answer = 0;

        return answer;
    }
}

// 0은 못가고 1만 갈 수 있다.
// (0,0)에서 시작
// 상하좌우로 움직인다.
// 가장 적게 움직여 도착해야한다.
// 못가면 -1

// queue에 시작점 넣기
// visited 처리

// while queue:
//     현재 위치 꺼내기

//     도착점이면 거리 반환

//     네 방향 확인:
//         범위 안인가?
//         벽이 아닌가?
//         방문 안 했는가?
//             방문 처리
//             queue에 추가

// return -1