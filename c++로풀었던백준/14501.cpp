#include<bits/stdc++.h>
using namespace std;
#define MAX 15
int n = 0, max_p = 0, dp[MAX], t[MAX], p[MAX];

void input(){
	cin >> n;
	for (int i = 0; i < n; i ++){
		cin >> t[i] >> p[i];
		dp[i] = 0;
	}
}

void solution(){
	input();
	for (int i = 0; i <= n; i ++){
		dp[i] = max(dp[i], max_p);
		
		if (t[i] + i <= n){
			dp[t[i] + i] = max(dp[t[i] + i], p[i] + dp[i]);
		}
		max_p = max(dp[i], max_p);
	}
	
	cout << max_p << "\n";
	
	cout << "============\n";
	
	for (int i = 0; i <= n; i ++){
		cout << dp[i] << "\n";
	}
}

int main(){
	solution();
}
