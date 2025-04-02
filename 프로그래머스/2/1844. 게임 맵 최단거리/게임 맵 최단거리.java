import java.util.*;

class Solution {
        int[] dx = {0, 0, -1, 1};
    int[] dy = {-1, 1, 0, 0};

    public int solution(int[][] map) {
        int answer = 0;
        int[][] visited = new int[map.length][map[0].length];
        int x = 0, y = 0, dist = 1, goal_x = map[0].length - 1, goal_y = map.length - 1;

        // 방문 여부 및 이동 가능 여부 초기화
        for (int i = 0; i < map.length; i++) {
            for (int j = 0; j < map[0].length; j++) {
                visited[i][j] = map[i][j];
            }
        }
        visited[y][x] = 0;

        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{x, y, dist});

        while (!q.isEmpty()) {
            int[] n = q.poll();
            int nx = n[0];
            int ny = n[1];
            int ndist = n[2];

            if (nx == goal_x && ny == goal_y) {
                return ndist;
            }

            for (int i = 0; i < 4; i++) {
                int nextX = nx + dx[i];
                int nextY = ny + dy[i];

                if (nextX >= 0 && nextY >= 0 && nextX < map[0].length && nextY < map.length && visited[nextY][nextX] == 1) {
                    visited[nextY][nextX] = 0; // 방문 표시
                    q.offer(new int[]{nextX, nextY, ndist + 1}); // 거리 1 증가
                }
            }
        }

        return -1;
    }
}