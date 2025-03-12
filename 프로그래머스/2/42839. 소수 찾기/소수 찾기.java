import java.util.*;
 
class Solution {
    List<Integer> nums = new ArrayList<>();
    boolean[] check;
    public int solution(String numbers) {
        int answer = 0;
        boolean num_check = true;
        check  = new boolean[numbers.length()];
        
        dfs(numbers, check, "");
        
        for (int i = 0; i < nums.size(); i ++){
            int num = nums.get(i);
            if (num > 1){
                num_check = check_number(num);
                if (num_check == true)  answer ++;   
            }
        }
        
        
        return answer;
    }
    
    public void dfs(String numbers, boolean[] check, String tmp){
        if (tmp.length() > 0){
            int num = Integer.parseInt(tmp);
            if (!nums.contains(num)){
                nums.add(num);
            }
        }
        
        for (int i = 0; i < numbers.length(); i ++){
            if (!check[i]){
                check[i] = true;
                tmp += numbers.charAt(i);
                dfs(numbers, check, tmp);
                check[i] = false;   
                tmp = tmp.substring(0, tmp.length() - 1);
            }
        }
    }
    
    public boolean check_number(int number){
        boolean check = true;
        for (int i = 2; i < number; i ++){
            if (number % i == 0)    check = false;
        }
        
        return check;
    } 
}