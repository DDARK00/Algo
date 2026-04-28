#include <iostream>
#include <queue>
#include <vector>
using namespace std;

template <typename T>
using min_pq=priority_queue<T,vector<T>,greater<T>>;

const long long INF=1LL<<60;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m, k;
    cin >> n >> m >> k;

    long long a, b, c;
    vector graph(n+1,vector<pair<long long, long long>>());
    for (int i=0; i<m; i++) {
        cin >> a >> b >> c;
        graph[a].push_back({c,b}); // w, v
    }

    vector dist(n+1, -1); // a b k
    vector<int> cnt(n+1,0);
    dist[1]=0;

    min_pq<pair<long long, long long>> pq;
    pq.push({0,1}); // w, v

    while (!pq.empty()) {
        auto [w, v]=pq.top();pq.pop();
        if (cnt[v]>=k) {
            continue;
        }
        cnt[v]++;
        if (cnt[v]==k) {
            dist[v]=w;
        }

        for (auto nxt : graph[v]) {
            auto [nw, nv]=nxt;
            if (cnt[nv]>=k) {
                continue;
            }
            pq.push({nw+w,nv});
        }
    }

    for (int i=1; i<n+1; i++) {
        if (cnt[i]==k) {
            cout << dist[i] << "\n";
        } else {
            cout << "-1\n";
        }
    }
    return 0;
}