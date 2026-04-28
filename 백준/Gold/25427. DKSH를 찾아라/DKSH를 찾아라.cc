#include <iostream>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;
    string s;
    cin>> s;
    long long cnt_d=0; // 10만
    long long cnt_dk=0; // 10만
    long long cnt_dks=0; // 10만
    long long answer=0;
    for (int i=0; i<n; i++) {
        if (s[i]=='D') {
            cnt_d++;
        } else if (s[i]=='K') {
            cnt_dk+=cnt_d;
        } else if (s[i]=='S') {
            cnt_dks+=cnt_dk;
        } else if (s[i]=='H') {
            answer+=cnt_dks;
        }
    }

    cout << answer;
    return 0;
}