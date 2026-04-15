#include <iostream>
#include <map>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    map<string, int> overtime;
    int n;
    cin >> n;
    string p, q;
    int answer=0;
    for (int i=0; i<n; i++) {
        cin >> p >> q;
        if (q=="-") {
            if (overtime[p]) {
                overtime[p]--;
            } else {
                answer++;
            }
        } else {
            overtime[p]++;
        }
    }

    for (auto k : overtime) {
        answer+=k.second;
    }
    cout << answer;
    return 0;
}