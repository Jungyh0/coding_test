import java.util.*;

class Solution {
   public int solution(int[] numbers, int target) {
        int answer = 0;
        int length = numbers.length;
       Queue<Integer> q = new LinkedList<>();
       
       q.offer(numbers[0]);
       q.offer(-numbers[0]);
       
       for (int i = 1; i < length; i ++){
           int size = q.size();
           for (int j = 0; j < size; j ++){
               int cur = q.poll();
               q.offer(cur + numbers[i]);
               q.offer(cur - numbers[i]);
            }
        }
       
       while (!q.isEmpty()){
           if (q.poll() == target){
               answer ++;
           }
       }
        return answer;
    }
}