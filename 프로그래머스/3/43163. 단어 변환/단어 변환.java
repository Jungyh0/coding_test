import java.util.*;

class Solution {

public int solution(String begin, String target, String[] words) {
    int answer = 0;
    Queue<String> q = new LinkedList<>();
    Set<String> visited = new HashSet<>();
    q.offer(begin);
    visited.add(begin);
    
    while (!q.isEmpty()) {
        int size = q.size();
        for (int i = 0; i < size; i++) {
            String s = q.poll();
            if (s.equals(target)) {
                return answer;
            }
            for (String w : words) {
                if (!visited.contains(w)) {
                    int same = 0;
                    for (int j = 0; j < s.length(); j++) {
                        if (s.charAt(j) == w.charAt(j)) {
                            same++;
                        }
                    }
                    if (same == s.length() - 1) {
                        q.offer(w);
                        visited.add(w);
                    }
                }
            }
        }
        answer++;
    }
    return 0;
}

}