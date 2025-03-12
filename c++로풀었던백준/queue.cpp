#include <bits/stdc++.h>
using namespace std;

#define MAX 1000

class que {
private:
    int front, rear, number;
    int* arr;

public:
    que() {
        arr = new int[MAX];
        front = 0;
        rear = -1;
        number = 0;
    }
    ~que() {
        delete[] arr;
    }
    void push(int num);
    void pop();
    void size();
    void empty();
    void back();
    void Front();
};

void que::push(int num) {
    if (number >= MAX) {
        return;
    }
    arr[++rear % MAX] = num;
    number++;
}

void que::pop() {
    if (number <= 0) {
        cout << -1 << endl;
        return;
    } else {
        cout << arr[front++ % MAX] << endl;
        number--;
    }
}

void que::size() {
    cout << number << endl;
}
void que::empty() {
    if (number == 0) {
        cout << 1 << endl;
    } else {
        cout << 0 << endl;
    }
}

void que::back() {
    if (number <= 0) {
        cout << -1 << endl;
        return;
    }
    int i = arr[rear % MAX];
    cout << i << endl;
}

void que::Front() {
    if (number <= 0) {
        cout << -1 << endl;
        return;
    }
    int i = arr[front % MAX];
    cout << i << endl;
}

int main() {
    int v = 0, num_ans = 0;
    string fun;
    que q;

    cin >> v;
    for (int i = 0; i < v; i++) {
        cin >> fun;
        if (fun == "push") {
            cin >> num_ans;
            q.push(num_ans);
        }
        if (fun == "front")
            q.Front();
        if (fun == "back")
            q.back();
        if (fun == "empty")
            q.empty();
        if (fun == "size")
            q.size();
        if (fun == "pop")
            q.pop();
    }
    return 0;
}
