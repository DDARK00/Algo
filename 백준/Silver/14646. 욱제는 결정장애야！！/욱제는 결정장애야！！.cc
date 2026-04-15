#include <iostream>
using namespace std;
int main() {
    int n;
    cin >> n;
    bool chk[n+1]{};
    int idx, ans = 0, temp = 0;
    for (int i=0; i<n*2; i++) {
        cin >> idx;
        if (chk[idx]){
            temp-=1;
        }else{
            temp+=1;
            chk[idx]=1;
            ans = max(ans, temp);
        }
        
    }
    cout << ans;
    return 0;
}