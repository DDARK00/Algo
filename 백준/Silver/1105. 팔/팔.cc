#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    string l, r;
    cin >> l >> r;
    // 1<=l<=r<=20억
    // 108 108 1
    // 108 109 0
    // 188 198 0
    int ans=0;
    l.insert(0,r.size()-l.size(),'0');
    int lk, rk;
    for (int i=0; i<r.size(); i++) {
        lk=l[i]-'0';
        rk=r[i]-'0';
        if (lk<rk){
            break;
        }else if (rk==8){
            ans+=1;
        }
    }
    cout << ans;
    return 0;
}