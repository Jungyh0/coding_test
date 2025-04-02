import java.util.*;

class Solution {
    public int[] solution(int[] prices) {
        int[] answer = {};
        answer = new int[prices.length];
        int idx = 0;
        Queue<Integer> q = new LinkedList<Integer>();

        for (int num : prices){
            q.offer(num);
        }

        while (!q.isEmpty()){
            int price = q.poll();
            for (int i = prices.length - q.size(); i < prices.length; i ++){
                if (price <= prices[i]){
                    answer[idx] ++;
                }
                else if (price > prices[i]) {
                    answer[idx]++;
                    break;
                }
            }
            idx ++;
        }
        return answer;
    }
}