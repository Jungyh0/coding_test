import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        int []answer = {};
        Stack<Integer> s = new Stack<>();
        
        s.push(arr[0]);
        for (int num : arr){
            if (s.peek() != num){
                s.push(num);
            }
        }
        answer = new int[s.size()];
        for (int i = s.size() - 1; i >= 0; i --){
            answer[i] = s.pop();
        }
        return answer;
    }
}