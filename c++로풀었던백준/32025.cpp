#include<bits/stdc++.h>
using namespace std;

int main(){
	int num1, num2, ans = 0;
	
	cin >> num1 >> num2;

	ans = min(num1, num2);	
	
	cout << ans * 100 / 2;
}
