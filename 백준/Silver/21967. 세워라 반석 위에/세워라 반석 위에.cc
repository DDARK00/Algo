#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    cin >> n;

    int arr[1000001];
    int mn=11, mx=0;
    
    int l=0, r, answer=1;
    for (r=0; r<n; r++) {
        cin >> arr[r];
        mx=max(arr[r],mx);
        mn=min(arr[r],mn);

        if (mx-mn<=2){
            continue;
        }
        answer=max(answer,r-l);
        // 현재값arr[r]mx or mn - 최대or최소 >2
        mn=arr[r], mx=arr[r];

        l=r;
        while (abs(arr[r]-arr[l])<=2){
            mx=max(arr[l],mx);
            mn=min(arr[l],mn);
            l--;
        }
        l++;
        mx=max(arr[l],mx);
        mn=min(arr[l],mn);
        // cout << mx << " mx/mn " << mn <<"\n";
        // cout << l << " l / r " << r << "\n";
        // answer=max(answer,r-l);
    }
    answer=max(answer,r-l);
    cout << answer;
    return 0;
}