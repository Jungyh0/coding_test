#include<bits/stdc++.h>
using namespace std;
#define MAX 5010
typedef pair<int, char> pill;

int n, len;
char view;
vector<pill> cats;

void input(){
	cin >> n;
	
	for (int i = 0; i < n; i ++){
		cin >> len >> view;
		cats.push_back (make_pair (len, view));
	}
}

void solve(){
	input();
}

int main(){
	solve();
}
