#include <iostream>
using namespace std;
 
int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
 
    int n, k, nxt=0;
    cin >> n;
    int ar[n];
    for (int i=0;i<n;i++) {
        cin>>ar[i];
    }
 
    bool chk = true;
    for (int i=0; i<n; i++) {
        if (nxt<ar[i]){
            chk=false;
            break;
        }
        if(cin.eof())break;
        cin >> k;
        nxt = max(nxt, ar[i]+k);
    }
    if (chk) {
        cout << "권병장님, 중대장님이 찾으십니다";
    }else{
        cout << "엄마 나 전역 늦어질 것 같아";
    }
    return 0;
}