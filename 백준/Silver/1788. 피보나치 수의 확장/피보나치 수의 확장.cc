#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int dp_p[1000001], dp_n[1000001];
    dp_p[0]=0;
    dp_p[1]=1;
    for (int i=2; i<1000001; i++) {
        dp_p[i]=(dp_p[i-1]+dp_p[i-2])%1000000000;
    }

    // f=0 =0 f-1 =-1 + f-2=1
    // fn-2-fn-1=fn
    dp_n[0]=0;
    dp_n[1]=1;
    for (int i=2; i<1000001; i++) {
        dp_n[i]=(dp_n[i-2]-dp_n[i-1])%1000000000;
    }

    int n;
    cin >> n;
    if (n>0){
        cout << 1 << "\n" << dp_p[n];
    } else {
        if (dp_n[-n]==0) {
            cout << 0 << "\n" << 0;
        } else if (dp_n[-n]>0) {
            cout << 1 << "\n" << dp_n[-n];
        } else {
            cout << -1 << "\n" << -dp_n[-n];
        }
    }
    return 0;
}