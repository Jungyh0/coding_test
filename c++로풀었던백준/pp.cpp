#include<bits/stdc++.h>
using namespace std;
#define MAX 1010

int n, arr[MAX], dp[MAX], len=0;

void input(){
	cin >> n;
	
	for (int i = 0; i < n; i++){
		cin >> arr[i];
	}
}

void solution(){
	
	for (int i = 0; i < n; i ++){
		dp[i]=1;
		for (int j = 0; j < i; j++){
			if(arr[i] > arr[j]){
				dp[i] = max(dp[i], dp[j]+1);
				
			}
		}
		len = max(dp[i], len);
	}
	cout << len;
}

int main(){
	input();
	solution();
}
