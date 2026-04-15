#include <iostream>
using namespace std;

void solve(){
    int n, tmp=0;
    cin >> n;
    string s;
    cin >> s;
    bool flag_minus=false, flag_plus=false, flag_answer=false;
    for (int i=1; i<2*n; i+=2) {
        if (s[i]=='-'){
            if (flag_minus) {
                flag_plus=true;
            }else{
                flag_minus=true;
            }
        }
        if (flag_minus&&s[i]=='+') {
            flag_plus=true;
        }
        if (flag_plus && (s[i+1]!='0')) {
            flag_answer=true;
            break;
        }
    }
    if (flag_answer) {
        cout << "NO" << "\n";
    }else{
        cout << "YES" << "\n";
    }
}
// 3-0-0-0+0
// 1+0-0-1
// 1+1-1-0
// 이게 진짜 맞는 풀이법임???
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int tc;
    cin >> tc;
    for (int i=0; i<tc; i++) {
        solve();
    }
    return 0;
}