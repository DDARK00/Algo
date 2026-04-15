#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n, k;
    cin >> n >> k;
    vector<int> hall(n+1,0);
    for (int i=0; i<n; i++) {
        cin >> hall[i+1];
    }
    sort(hall.begin(),hall.end());
    vector<int> dist(n);
    for (int i=0; i<n; i++) {
        dist[i]=hall[i+1]-hall[i];
    }
    sort(dist.begin(),dist.end());
    long long answer=0;
    for (int i=0; i<n-k; i++) {
        answer+=dist[i];
    }

    cout << answer;
    return 0;
}