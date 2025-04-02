import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        int day = 0;
        int[] answer = {};
        List<Integer> ans_list = new ArrayList<>();
        int p_front, s_front;
        Queue<Integer> q_pro = new LinkedList<Integer>();
        Queue<Integer> q_speed = new LinkedList<Integer>();

        for (int num : progresses)  q_pro.add(num);
        for (int num : speeds)  q_speed.add(num);

        while (!q_pro.isEmpty() && !q_speed.isEmpty()){
            int count = 0;
            day ++;
            p_front = q_pro.remove();
            s_front = q_speed.remove();

            while (p_front + s_front * day < 100){
                day ++;
            }
            count ++;

            while (!q_pro.isEmpty() && !q_speed.isEmpty() && q_pro.peek() + (q_speed.peek() * day) >= 100){
                q_pro.remove(); q_speed.remove();
                count++;
            }
            ans_list.add(count);
        }
        
        answer = new int[ans_list.size()];
        for (int i = 0; i < answer.length; i++) {
            answer[i] = ans_list.get(i);
        }
        
        return answer;
    }
}