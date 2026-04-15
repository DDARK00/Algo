#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int n, m;
vector<int> answer(100000,0);
vector<queue<int>> sushi(200001,queue<int>());

void solve(){
    int b, idx;
    for (int i=0; i<m; i++) {
        cin >> b;
        if (sushi[b].empty()) continue;
        idx=sushi[b].front();sushi[b].pop();
        answer[idx]++;
    }
}

void print(){
    for (int i=0; i<n; i++) {
        cout << answer[i] << " ";
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin >> n >> m;

    // init
    int k, a;
    for (int i=0; i<n; i++) {
        cin >> k;
        for (int j=0; j<k; j++) {
            cin >> a;
            sushi[a].push(i);
        }
    }
    solve();
    print();
    return 0;
}