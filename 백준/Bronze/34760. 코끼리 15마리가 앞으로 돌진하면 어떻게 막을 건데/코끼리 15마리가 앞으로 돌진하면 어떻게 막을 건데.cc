#include <iostream>
using namespace std;

int main() {
    long long ko, answer=0;
    for (int i=0; i<14; i++) {
        cin >> ko;
        if (ko>=answer) {
            answer=ko+1;
        }
    }
    cin >> ko;
    cout << max(ko,answer);
    return 0;
}