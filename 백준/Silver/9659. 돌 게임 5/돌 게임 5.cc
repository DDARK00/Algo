#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    // 1 1 1
    // 2 11 2
    // 3 3 111 1
    // 4 13 31 2
    // 5 311 11111 131

    long long n;
    cin >> n;
    if (n%2) {
        cout << "SK";
    } else {
        cout << "CY";
    }
    return 0;
}