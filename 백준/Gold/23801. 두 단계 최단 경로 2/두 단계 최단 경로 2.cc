#include <iostream>
#include <queue>
#include <vector>
using namespace std;

template <typename T>
using min_pq=priority_queue<T, vector<T>, greater<T>>;

const long long INF=1LL << 60;;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    long long n, m, u, v, w;
    cin >> n >> m;
    vector graph(n+1, vector<pair<long long,long long>>());
    for (int i=0; i<m; i++) {
        cin >> u >> v >> w;
        graph[u].push_back({w,v});
        graph[v].push_back({w,u});
    }

    long long x, z, p, tmp;
    cin >> x >> z >> p;

    vector<long long> y_vc;
    for (int i=0; i<p; i++) {
        cin >> tmp;
        y_vc.push_back(tmp);
    }

    // w, v
    // x->y y->z
    // x->y
    min_pq<pair<long long,long long>> pq;
    pq.push({0,x});
    vector<long long> dist_x_y(n+1, INF); // 10만, 100만
    dist_x_y[x]=0;
    while (!pq.empty()){
        auto [w, v]=pq.top();
        pq.pop();
        if (dist_x_y[v]<w) {
            continue;
        }
        for (auto nxt : graph[v]) {
            auto [nw, nv]=nxt;
            if (dist_x_y[nv]>nw+w) {
                dist_x_y[nv]=nw+w;
                pq.push({nw+w,nv});
            }
        }
    }

    // z-> y
    pq={};
    vector<long long> dist_z_y(n+1, INF);
    dist_z_y[z]=0;
    pq.push({0,z});

    while (!pq.empty()){
        auto [w, v]=pq.top();
        pq.pop();
        if (dist_z_y[v]<w) {
            continue;
        }
        for (auto nxt : graph[v]) {
            auto [nw, nv]=nxt;
            if (dist_z_y[nv]>nw+w) {
                dist_z_y[nv]=nw+w;
                pq.push({nw+w,nv});
            }
        }
    }

    long long answer=INF;
    for (auto k : y_vc) {
        answer=min(answer,dist_x_y[k]+dist_z_y[k]);
    }
    if (answer==INF) {
        answer=-1;
    }
    cout << answer;
    return 0;
}