#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n, c;
    cin >> n;

    vector<int> vc;
    for (int i=0; i<n; i++) {
        cin >> c;
        vc.push_back(c);
    }

    int answer=0;
    sort(vc.begin(),vc.end(),greater<int>());
    for (int i=0; i<n; i++) {
        if (i%3==2) continue;
        answer+=vc[i];
    }

    cout << answer;
    return 0;
}