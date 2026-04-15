#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n, k;
    cin >> n >> k;
    int temp, before;
    cin >> before;
    vector<int> vc;
    vc.push_back(0);
    vc.push_back(1);
    for (int i=0; i<n-1; i++) {
        cin >> temp;
        vc.push_back(temp-before-1);
        vc.push_back(1);
        before=temp;
        }
    // n 100000
    sort(vc.begin(),vc.end());
    int answer=0;
    for (int i=0; i<n*2-k+1; i++) {
        // cout << vc[i] << " ";
        answer+=vc[i];
    }
    cout << max(n,answer);
    return 0;
}