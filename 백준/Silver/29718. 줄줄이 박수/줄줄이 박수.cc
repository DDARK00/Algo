#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m, temp;
    cin >> n >> m;
    vector<int> pre_sum(m+m+1,0);
    for (int i=0; i<n; i++) {
        for (int j=0; j<m; j++) {
            cin >> temp;
            pre_sum[j]+=temp;
        }
    }
    
    int k, answer=0, now=0;
    cin >> k;
    for (int i=m-1; i>=0; i--) {
        now-=pre_sum[i+k];
        now+=pre_sum[i];
        answer = max(answer,now);
    }

    cout << answer;
    return 0;
}