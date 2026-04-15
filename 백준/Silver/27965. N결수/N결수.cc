#include <iostream>
#include <cmath>
#include <string>
using namespace std;
// 1 12 123 1234 7
// 0 5   53   40+4
// 1 5    4   2
int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, k;
    cin >> n >> k;
    long long answer=0;
    for (int i=1; i<n+1; i++) {
        string s=to_string(i);
        answer*=((long long)pow(10,s.size())%k);
        answer+=i;
        answer%=k;
    }

    cout << answer;
    return 0;
}