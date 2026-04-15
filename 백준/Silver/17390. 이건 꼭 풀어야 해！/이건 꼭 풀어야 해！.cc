#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n, q;
    cin >> n >> q;

    int nums[300001];
    for (int i=0; i<n; i++) {
        cin >> nums[i];
    }
    sort(nums,nums+n);

    int pf_sum[300001];
    pf_sum[0]=0;
    for (int i=0; i<n; i++) {
        pf_sum[i+1]=pf_sum[i]+nums[i];
    }

    int l, r;
    for (int i=0; i<q; i++) {
        cin >> l >> r;
        cout << pf_sum[r]-pf_sum[l-1] << "\n";
    }
    return 0;
}