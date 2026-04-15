#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    string s;
    cin >> s;

    long long answer=0;
    // 100000*100000 1e10
    char before;
    long long a_cnt=1;
    long long z_cnt=0;
    // answer += a*z
    for (int i=0; i<s.size(); i++) {
        if (s[i]=='A') {
            if (s.size()-i<26) break;
            if (s[i+1]=='A') {
                a_cnt++;
                continue;
            }
            before='A';
            for (int j=i+1; j<s.size(); j++) {
                if (s[j] != before && s[j]-1 != before) break;
                if (s[j]=='Z') {
                    z_cnt++;
                }
                before = s[j];
            }
            answer+= a_cnt*z_cnt;
            a_cnt=1;
            z_cnt=0;
        }
    }

    cout << answer;
    return 0;
}