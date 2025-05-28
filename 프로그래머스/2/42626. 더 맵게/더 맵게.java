import java.util.*;

class Solution {
    PriorityQueue<Integer> pq = new PriorityQueue<>();
    public int solution(int[] scoville, int K) {
        int answer = 0;
        for (int i : scoville){
            pq.offer(i);
        }
        if (pq.size() > 1){
           while (pq.peek() < K){
               if (pq.size() > 1){
                   answer ++;
                    pq.offer(shake(pq.poll(), pq.poll()));
                }
               else break;
            } 
        }  
        if (pq.peek() < K)  return -1;
        return answer;
    }
    
    public int shake(int f1, int f2){
        int num = f1 + (f2 * 2);
        
        return num;
    }
}