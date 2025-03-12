#include<bits/stdc++.h>
using namespace std;

int n, max_num = INT_MIN, min_num = INT_MAX;
int opt[4], nums[11];

void input(){
	cin >> n;
	for (int i = 0; i < n; i ++){
		cin >> nums[i];
	}
	
	for (int i = 0; i < 4; i ++){
		cin >> opt[i];
	}
}

void calc(int result, int idx){
	if (idx == n){
		if (result > max_num){
			max_num = result;
		}
		if (result < min_num){
			min_num = result;
		}
		return;
	}
	
	for (int i = 0; i < 4; i ++){
		if (opt[i] > 0){
			opt[i] --;
			if (i == 0){
				calc(result + nums[idx], idx + 1);
			}
			else if (i == 1){
				calc(result - nums[idx], idx + 1);
			}
			else if (i == 2){
				calc(result * nums[idx], idx + 1);
			}
			else {
				if (nums[idx] != 0)
					calc(result / nums[idx], idx + 1);
			}
			opt[i] ++;
		}
	}
	return;
	
}

void solution(){
	input();
	calc(nums[0], 1);
	
	cout << max_num << "\n" << min_num;
	
	
}

int main(){
	solution();
}
