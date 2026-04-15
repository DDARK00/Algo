#include <iostream>
using namespace std;

int main() {
    int n, a, b;
    cin >> n;
    cout << "? 1 \n" << flush;
    cin >> a;
    cout << "? " << n << "\n" << flush;
    cin >> b;
    // 0000 0
    // 0010 0
    // 0011 1
    // 0111 1
    // 1001 0
    // 1000 -1
    // -a + b
    cout << "! " << b-a;
    return 0;
}