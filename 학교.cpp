#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define MAX 100010

ll n, x, arr[MAX];

void input(){
	cin >> n >> x;
	
	for (int i = 0; i < n; i++){
		cin >> arr[i];
	}
}

void solution(){
	ll small = 1e18;
	
	for (int i = 0; i < n-1; i++){
		ll num = x * (arr[i] + arr[i+1]);
		small = min(num, small);
	}

	cout << small;
}

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	input();
	solution();
	
	return 0;
}
