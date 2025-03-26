import java.util.*;

class Solution {
    static List<String> rute = new ArrayList<>();
    static boolean[] visited;
    
    public static String[] solution(String[][] tickets) {
    	Arrays.sort(tickets, (a, b) -> {
            if (a[0].equals(b[0])) return a[1].compareTo(b[1]);
            return a[0].compareTo(b[0]);
        });
        String[] answer;
        visited = new boolean[tickets.length];
        rute.add("ICN");
        dfs(tickets, "ICN");       
        answer = rute.toArray(new String[rute.size()]);
        return answer;
    }
    
    public static void dfs(String[][] tickets, String st){
    
    	
        for (int i = 0; i < tickets.length; i ++){
        	if (st.equals(tickets[i][0])){
        		if (visited[i] == false && rute.size() < tickets.length + 1) {
                    rute.add(tickets[i][1]);
                    visited[i] = true;
                    dfs(tickets, tickets[i][1]);
                    visited[i] = false;
        		}
            }
        	else if(rute.size() == tickets.length + 1) {
        		return;
        	}
        	else if (!st.equals(tickets[i][0]) && i == tickets.length - 1) {
        		rute.remove(rute.size() - 1);
            	return;
            }
        	
        }
    }
    
}