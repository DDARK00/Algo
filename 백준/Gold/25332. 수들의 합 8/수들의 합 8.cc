#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n, k;
    cin >> n;
    vector<long long> vc(n+1);
    vc[0]=0;
    for (int i=1; i<n+1; i++) {
        cin >> k;
        vc[i]=k;
    }
    for (int i=1; i<n+1; i++) {
        cin >> k;
        vc[i]-=k;
    }

    for (int i=1; i<n+1; i++) {
        vc[i]=vc[i-1]+vc[i];
    }

    unordered_map<long long, long long> chk;
    for (int i=0; i<n+1; i++) {
        chk[vc[i]]++;
    }

    long long answer=0;
    for (auto p : chk) {
        auto [k,v]=p;
        if (v>1) {
            answer+=v*(v-1)/2;
        }
    }

    cout << answer << "\n";
    return 0;
}