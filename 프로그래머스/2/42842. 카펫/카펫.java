import java.util.*;

class Solution {
    public static int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        int sum = brown + yellow;
        int half = sum / 2;
        int r = 0, c = 0;
        for (int i = half; i >=3 ; i --){
            c = sum / i;
            r = sum / c;
            if (c < r)  continue;
            int line = 2 * (r + c) - 4;
            if (line == brown){
                break;
            }
        }
        answer[0] = c;
        answer[1] = r;
        return answer;
    }
}