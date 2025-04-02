import java.util.*;

class Solution {
    static int[][] maps;
	static boolean[] visited;
	static PriorityQueue<Integer> pq = new PriorityQueue<>();
	
	public static int solution(int n, int[][] wires) {
		int answer;
		maps = new int[n + 1][n + 1];
		visited = new boolean[n + 1];
		makemaps(wires);
		int len1 = 0, len2 = 0;

		
		for (int i = 1; i < maps.length; i ++) {
			for (int j = 0; j < maps[0].length; j ++) {
				if (maps[i][j] == 1) {
					maps[i][j] = 0;	
					maps[j][i] = 0;	
					len1 = search(maps, 1);
					len2 = n - len1;
					pq.offer(sub(len1, len2));
					maps[i][j] = 1;
					maps[j][i] = 1;
				}
			}
		}
		
		answer = pq.poll();
		return answer;
	}
	
	public static int sub(int n1, int n2) {
		int result = 0;
		
		if (n1 > n2) {
			result = n1 - n2;
		}
		
		else result = n2 - n1;
		
		return result;
	}
	
	public static int search(int[][] maps, int index) {
		int nodes = 0;
		if (index == 1) {	
			nodes ++;
			visited[1] = true;
		}
		
		for (int i = 1; i < maps[0].length; i ++) {
			if (maps[index][i] == 1 && !visited[i]) {
				visited[i] = true;
				nodes ++;
				nodes += search(maps, i);
				visited[i] = false;
			}
		}
		
		return nodes;
	}
	
	public static int check(int[] nums) {
		int check = -1;
		
		for (int i = 0; i < nums.length; i ++) {
			if (nums[i] == 1)	check = i;
		}
		
		return check;
	}
	
	public static void makemaps(int[][] wires) {
		for (int i = 0; i < wires.length; i ++) {
			maps[wires[i][0]][wires[i][1]] = 1;
			maps[wires[i][1]][wires[i][0]] = 1;
		}
	}
}