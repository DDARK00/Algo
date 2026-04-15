#include <iostream>
#include <vector>
#include <queue>
#include <tuple>
using namespace std;
const int INT_MAX = 2000001; // 100000 * 20

int n, m, a, b, c;
vector<vector<pair<int,int>>> graph(100001,vector<pair<int,int>>());

bool dijk(int limit) {
    vector<int> dist(n+1, INT_MAX);
    priority_queue<pair<int,int>,vector<pair<int,int>>,greater<>> pq;
    dist[a]=0; // w,v
    pq.push({0,a}); // a to b in limit

    while (!pq.empty()) {
        auto [w,v]=pq.top();pq.pop();
        if (w>dist[v]) {
            continue;
        }

        for (auto [nv, nw] : graph[v]) {
            if (nw > limit) continue;
            if (dist[nv] > w + nw) {
                dist[nv] = w + nw;
                pq.push({w+nw, nv});
            }
        }
    }
    return dist[b]<=c;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> n >> m >> a >> b >> c;

    int p, q, w;
    for (int i=0; i<m; i++) {
        cin >> p >> q >> w;
        graph[p].push_back({q,w});
        graph[q].push_back({p,w}); // v w
    }

    // 1 ≤ 골목 별 수금액 ≤ 20
    // 최대 비용 내에서 전체 비용이 최소(도달 가능)
    int l=1, r=20, answer=-1;
    while (l<=r) {
        int mid=(l+r) / 2;
        if (dijk(mid)) {
            answer=mid;
            r=mid-1;
        } else {
            l=mid+1;
        }
    }
    cout << answer;

    return 0;
}