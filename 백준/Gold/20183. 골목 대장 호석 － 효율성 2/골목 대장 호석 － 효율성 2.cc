#include <iostream>
#include <vector>
#include <queue>
#include <tuple>
using namespace std;
const long long MAX_VALUE = 1e14;

int n, m, a, b;
long long c;
vector<vector<pair<int,int>>> graph(100001,vector<pair<int,int>>());

bool dijk(long long limit) {
    vector<long long> dist(n+1, MAX_VALUE);
    priority_queue<pair<long long,int>,vector<pair<long long,int>>,greater<>> pq;
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

    long long l=1, r=1e9, answer=-1;
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