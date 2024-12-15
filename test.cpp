#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define MAX 1e5

ll n, len=0;
ll arr[MAX], dp[MAX];

void input(){
	cin >> n;
	
	for (int i =0; i < n; i++){
		cin >> arr[i];
	}
}

void solution(){
	arr.sort(arr, arr+n);
	ll front = 0, rear = n, mid = (rear - (rear - front) ) /  2;
}

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	input();
	solution();
	
	return 0;
}
