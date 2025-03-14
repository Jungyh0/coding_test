import java.util.*;

class Solution {
    static int x_max = 102;
    static int y_max = 102;
    static boolean visited[][]; 
    static int[][] map;
    public int solution(int[][] rectangle, int characterX, int characterY, int itemX, int itemY) {
        map = new int[x_max][y_max];
        visited = new boolean[map.length][map[0].length];
        drawing_map(rectangle, map);
        return bfs(characterX * 2, characterY * 2, itemX * 2, itemY * 2) / 2;
    }
    
    public static void drawing_map(int[][] rectangle, int[][] map) {
        for (int[] sample : rectangle) {
            int st_x = sample[0] * 2, end_x = sample[2] * 2;
            int st_y = sample[1] * 2, end_y = sample[3] * 2;
            
            for (int i = st_x; i <= end_x; i++) {
                for (int j = st_y; j <= end_y; j++) {
                    map[i][j] = 1;
                }
            }
        }
        
        for (int[] sample : rectangle) {
            int st_x = sample[0] * 2, end_x = sample[2] * 2;
            int st_y = sample[1] * 2, end_y = sample[3] * 2;

            for (int i = st_x + 1; i < end_x; i++) {
                for (int j = st_y + 1; j < end_y; j++) {
                    map[i][j] = 0;
                }
            }
        }
    }
    
    public static int bfs(int character_x, int character_y, int itemX, int itemY){
        int[] range_x = new int[]{1, -1, 0, 0};
        int[] range_y = new int[]{0, 0, 1, -1};
        Queue<int[]> node = new LinkedList<>();
        visited[character_x][character_y] = true;
        node.offer(new int[]{character_x, character_y, 0});
        
        while (!node.isEmpty()){
            int[] tmp = node.poll();
            int x = tmp[0];
            int y = tmp[1];
            int count = tmp[2];
            if (x == itemX && y == itemY) {
                return count;
            }

            for (int i = 0; i < 4; i ++){
                int new_x = x + range_x[i];
                int new_y = y + range_y[i];
                if (new_x < 0 || new_y < 0 || new_x >= x_max || new_y >= y_max || map[new_x][new_y] == 0){
                    continue;
                }
                if (visited[new_x][new_y]) {
                    continue;
                }
                visited[new_x][new_y] = true;
                node.offer(new int[]{new_x, new_y, count + 1});
            }
        }
        return -1;
    }
}