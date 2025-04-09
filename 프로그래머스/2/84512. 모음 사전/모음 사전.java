import java.util.*;

class Solution {
    public static char[] words = new char[]{'A', 'E', 'I', 'O', 'U'};
    List<String> list = new ArrayList<>();
    public int solution(String word) {
        int answer = 0;
        dfs("", 0, word);
        answer = list.indexOf(word);
        return answer;
    }
    
    public void dfs(String add, int len, String word){
        list.add(add);
        if (add.equals(word)){
            return;
        }
        if (add.length() == 5){
            return;
        }
        for (int i = 0; i < words.length; i ++){
            dfs(add + words[i], len + 1, word);
        }
    }
}