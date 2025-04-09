import java.util.*;

class Solution {
    public long solution(int n, int[] times) {
        long answer = 0;
        Arrays.sort(times);
        long start = 0, end = times[times.length - 1] * (long)n;
        answer = bsearch(start, end, n, times);
        return answer;
    }
    
    public long bsearch(long start, long end, int n, int[] times){
        long answer = 0;
        while(start <= end){
            long mid = (start + end) / 2;
            long num = 0;
            
            for (int i = 0; i < times.length; i ++){
                num += mid / times[i];
            }
            
            if (num < n){
                start = mid + 1;
            }
            else{
                end = mid - 1;
                answer = mid;
            }
        }
        
        return answer;
    }
}