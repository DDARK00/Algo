#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n, k;
    cin >> n;

    vector<pair<int,int>> namu(n);
    for (int i=0; i<n; i++) {
        cin >> k;
        namu[i].second=k;
    }

    for (int i=0; i<n; i++) {
        cin >> k;
        namu[i].first=k;
    }
    sort(namu.begin(),namu.end());

    long long answer=0;
    for (int i=0; i<n; i++) {
        answer+=namu[i].second;
        answer+=namu[i].first*i;
    }

    cout << answer;
    return 0;
}