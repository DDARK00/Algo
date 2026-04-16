#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n, m;
    cin >> n;
    int sound[1001]{};
    for (int i=0; i<n; i++) {
        cin >> sound[i];
    }
    cin >> m;
    int dream[1001]{};
    for (int i=0; i<m; i++) {
        cin >> dream[i];
    }


    int ans_mn=1001, ans_mx=-1;
    for (int i=0; i<m; i++) { // st idx
        if (sound[0]!=dream[i]) {
            continue;
        }

        for (int j=1; i+j<m; j++) { // tempo
            int target=1;
            for (int k=i+j; k<m; k+=j) { // step
                if (sound[target]==dream[k]) {
                    target++;
                    if (target==n) {
                        ans_mn=min(ans_mn,j);
                        ans_mx=max(ans_mx,j);
                    }
                } else {
                    break;
                }
            }
        }
    }

    if (ans_mn==1001 || ans_mx==-1) {
        cout << -1;
    } else {
        cout << ans_mn-1 << " " << ans_mx-1;
    }
    return 0;
}