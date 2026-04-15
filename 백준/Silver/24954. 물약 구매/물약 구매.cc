#include <iostream>
#include <vector>
using namespace std;

int n;
int potion[11]; // 가격
int dc_money[11];
vector<vector<pair<int,int>>> discount(11); // i를 사면 a가 b만큼 할인
int answer=10001;
bool visited[11];

void dfs(int depth, int cost){
    if (cost>answer) return;
    if (depth==n) {
        answer=min(cost,answer);
        return;
    }
    for (int i=1; i<n+1; i++) {
        if (visited[i]) continue;
        visited[i]=1;
        for (auto k : discount[i]) {
            dc_money[k.first]+=k.second;
        }
        dfs(depth+1, cost+max(1,potion[i]-dc_money[i]));
        for (auto k : discount[i]) {
            dc_money[k.first]-=k.second;
        }
        visited[i]=0;
    }
}

void solve(){
    dfs(0,0); // depth, cost
    cout << answer;
}

// init
int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin >> n;
    for (int i=1; i<n+1; i++) {
        cin >> potion[i];
    }
    int p, a, d;
    for (int i=0; i<n; i++) {
        cin >> p;
        for (int j=0; j<p; j++) {
            cin >> a >> d;
            discount[i+1].push_back({a,d});
        }
    }
    // n=10 10!
    solve();
    return 0;
}