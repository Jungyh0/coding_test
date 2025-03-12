#include <bits/stdc++.h>
using namespace std;


string toLowerCase(string str) {
    for (char &c : str) {
        if (c >= 'A' && c <= 'Z') {
            c = c - 'A' + 'a';
        }
    }
    return str;
}


bool isPalindrome(const string &str) {
    int num = str.length();
    for (int i = 0; i < num / 2; i++) {
        if (str[i] != str[num - i - 1]) {
            return false;
        }
    }
    return true;
}

void input(int counter) {
    string input_str;
    for (int i = 0; i < counter; i++) {
        getline(cin, input_str);
        input_str = toLowerCase(input_str);
        if (isPalindrome(input_str)) {
            cout << "YES" << "\n";
        } else {
            cout << "NO" << "\n";
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int counter;
    cin >> counter;
    cin.ignore();
    input(counter);

    return 0;
}

