#include <iostream>
using namespace std;

void solve(int tc){
    int n;
    cin >> n;
    cout << "Case #" << tc << ": ";
    if (n==0){
        cout << "INSOMNIA\n";
        return;
    }

    int answer=1, k=n;
    bool chk[10]{};
    while (true) {
        while (k>0) {
            chk[k%10]=1;
            k/=10;
        }

        int cnt=0;
        for (int i=0; i<10; i++) {
            cnt+=chk[i];
        }

        if (cnt==10) {
            cout << answer*n << "\n";
            return;
        }
        answer++;
        k=answer*n;
    }
    
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int t;
    cin >> t;
    for (int i=1; i<t+1; i++) {
        solve(i);
    }
    return 0;
}