#include<bits/stdc++.h>
using namespace std;

vector<int> dp, lis;
int n = 0, idx = 0;

void input(){
	cin >> n;
	
	for (int i = 0; i < n; i ++){
		int num = 0;
		cin >> num;
		lis.push_back(num);
	}
	dp.push_back(lis.front() );
}

int test(int key) {
    int st = 0, rear = dp.size() - 1, mid;
    while (st <= rear) {
        mid = st + (rear - st) / 2;
        if (dp[mid] >= key) {
            rear = mid - 1;
        } else {
            st = mid + 1;
        }
    }
    return st;
}

void calc(){
	input();
	
	for (int i = 1; i < n; i ++){
		if (lis[i] > dp.back() ){
			dp.push_back(lis[i]);
		}
		else {
			idx = test(lis[i]);
			cout << "index: " << idx << "\n";
			dp[idx] = lis[i];
		}
	}
	
	cout << dp.size();
}

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	calc();
}
