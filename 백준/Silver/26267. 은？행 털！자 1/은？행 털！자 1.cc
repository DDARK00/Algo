#include <iostream>
#include <unordered_map>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    long long answer=0;
    cin >> n;
    unordered_map<int, long long> before;

    int x, t, c;
    for (int i=0; i<n; i++) {
        cin >> x >> t >> c;
        before[x-t]+=c;
        answer = max(answer, before[x-t]);
    }

    cout << answer;
    return 0;
}