import java.util.*;

class Solution {
    static boolean[] visited;
    static PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
    public int solution(int k, int[][] dungeons) {
        int result = 0;
        visited = new boolean[dungeons.length];
        
        for (int i = 0; i < dungeons.length; i ++){
        	int kk = k, rr = result;
            if (kk >= dungeons[i][0]){
                visited[i] = true;
                kk -= dungeons[i][1];
                rr ++;
                dfs(kk, rr, dungeons);
                visited[i] = false;
            }
            else{
                continue;
            }
        }
        result = pq.poll();
        return result;
    }
    
    static void dfs(int k, int result, int[][] dungeons){
        Queue<int[]> node = new LinkedList<>();
        
        node.offer(new int[]{k, result});
        while(!node.isEmpty()){
            int[] sample = node.poll();
            int kk = sample[0];
            int rr = sample[1];
            for (int i = 0; i < dungeons.length; i ++){
                if (!visited[i]){
                    if (kk >= dungeons[i][0]){
                        kk -= dungeons[i][1];
                        rr ++;
                        visited[i] = true;
                        dfs(kk, rr, dungeons);
                        rr --;
                        kk += dungeons[i][1];
                        visited[i] = false;
                    }
                }
            }
            pq.offer(rr);
        }
    }
}