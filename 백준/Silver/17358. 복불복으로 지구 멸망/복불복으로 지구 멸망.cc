#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    cin >> n;

    long long answer=1;

    // n=4 3 x 1 x
    // 6   5 x 3 x 1
    while (n>0) {
        answer*= n-1;
        answer%=(long long)(1e9+7);
        n-=2;
    }

    cout << answer;
    return 0;
}