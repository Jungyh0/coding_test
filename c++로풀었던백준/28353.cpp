#include<bits/stdc++.h>
using namespace std;

void solve(){
	int n, k, ans = 0, x;
	vector<int> cats;
	
	cin >> n >> k;
	
	for (int i = 0; i < n; i ++){
		cin >> x;
		cats.push_back(x);
	}
	
	sort (cats.begin(), cats.end() );

	int start = 0, end = n - 1;
	while (start < end){
		if (cats[start] + cats[end] <= k){
			ans ++;
			end --;
			start ++;
		}
		else end --;
	}
	cout << ans;
}

int main(){
	solve();
}
