#include<bits/stdc++.h>
#define MAX 10000
using namespace std;

class stack{
private:
	int top,number;
	int* arr;
		
public:
	Stack(){
		arr=new int[MAX];	top=-1;	number=0;
	}
	~Stack(){
		delete[] arr;
	}
	void push(int num)();
	void pop();
	void size();
	void empty();
	void top();
};



int main(){
	
}
