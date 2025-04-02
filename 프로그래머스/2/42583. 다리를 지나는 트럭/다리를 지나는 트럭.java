import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int n_weight = 0;
        int time = 0;
        int idx = 0;

        Queue<Integer> q = new LinkedList<>();

        for (int i = 0; i < bridge_length; i++) {
            q.offer(0);
        }

        while (idx < truck_weights.length || n_weight > 0) {
            time++;

            n_weight -= q.poll();

            if (idx < truck_weights.length) {
                if (n_weight + truck_weights[idx] <= weight) {
                    q.offer(truck_weights[idx]);
                    n_weight += truck_weights[idx];
                    idx++;
                } else {
                    q.offer(0);
                }
            }
        }

        return time;
    }
}
