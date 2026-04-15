#include <iostream>
#include <vector>
#include <numeric>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    cin >> n; // 20000

    vector<int> vc;
    vector<int> num(20001);
    vector<bool> visited(20001,0);
    for (int i=1; i<n+1; i++) {
        cin >> num[i];
    }

    for (int i=1; i<n+1; i++) {
        if (!visited[i]) {
            visited[i]=1;
            int target=num[i], len=0;
            while (target!=i) {
                 visited[target]=1;
                 len++;
                 target=num[target];
             }
            if (len!=0) {
                vc.push_back(len+1);
            }
        }
    }

    long long answer=1; // 1~2e9?
    for (int i=0; i<vc.size(); i++) {
        answer=answer*vc[i]/gcd(answer,vc[i]);
    }

    cout << answer;
    return 0;
}