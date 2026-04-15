#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n, m;
    cin >> n;
    int score[100001];
    score[0]=0;
    for (int i=1; i<n+1; i++) {
        cin >> score[i];
    }

    int pre_sum[100001];
    for (int i=1; i<n+1; i++) {
        pre_sum[i]=pre_sum[i-1]+(score[i-1]>score[i]);
        // cout << "i : " << i << " / " << pre_sum[i]<<"\n";
    }
    pre_sum[n+1]=pre_sum[n];
    cin >> m;
    int a, b;
    for (int i=0; i<m; i++) {
        cin >> a >> b;
        if (a==b) {
            cout << 0 << "\n";
        }else{
            cout << pre_sum[b]-pre_sum[a] << "\n";
        }
    }
    return 0;
}