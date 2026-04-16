#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int n, tmp;
    long long pre=0, answer=0;
    cin >> n;
    for (int i=0; i<n; i++) {
        cin >> tmp;
        answer+=pre*tmp;
        answer%=1000000007;
        pre+=tmp;
    }
    cout << answer;
    return 0;
}