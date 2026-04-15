#include <iostream>
using namespace std;

int main() {
    string s;
    cin >> s;

    int answer=0, cnt=0;
    for (int i=0; i<s.size(); i++) {
        if (s[i]=='(') {
            cnt++;
        } else if (cnt==0) {
            answer++;
        } else {
            cnt--;
        }
    }

    cout << answer+cnt;
    return 0;
}