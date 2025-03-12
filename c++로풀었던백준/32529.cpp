#include<bits/stdc++.h>
using namespace std;

int n, m, sum = 0;
vector<int> vec;

void input(){
	cin >> n >> m;
	for (int i = 0; i < n; i ++){
		int ans = 0;
		cin >> ans;
		vec.push_back(ans);
	}
}

void solution(){
	input();
	while(sum < m){
		sum += vec[--n];
		if (n < 0){
			cout << -1;
			return;
		}
	}
	cout << n + 1;
}

int main(){
	solution();
}
