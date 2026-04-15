#include <iostream>
#include <queue>
#include <vector>
#include <tuple>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n, m;
    cin >> n >> m; // v, e
    vector<int> is_view(n);
    for (int i=0; i<n; i++) {
        cin >> is_view[i];
    }

    is_view[n-1]=0; // nexus
    vector<vector<pair<int, int>>> graph(100000);

    int v1, v2, t;
    for (int i=0; i<m; i++) {
        cin >> v1 >> v2 >> t;
        if (is_view[v1] || is_view[v2])continue;
        // w, v
        graph[v1].push_back({t, v2});
        graph[v2].push_back({t, v1});
    }

    const auto cmp = [](auto a, auto b){return a.first>b.first;};
    priority_queue<pair<long long, int>, vector<pair<long long, int>>, decltype(cmp)> pq(cmp);
    pq.push({0,0});

    vector<long long> dist(n, 3e10+1);
    // 300000 * 100000 300억
    dist[0]=0;

    int v, nv;
    long long w, nw;
    while (!pq.empty()){
        tie(w, v)=pq.top();pq.pop();
        if (dist[v]<w) continue;
        for (auto k : graph[v]) {
            tie(nw, nv) = k;
            if(dist[nv]>w+nw){
                dist[nv]=w+nw;
                pq.push({w+nw, nv});
            }
        }
    }

    if (dist[n-1]==3e10+1){
        cout << "-1";
    }else{
        cout << dist[n-1];
    }
    return 0;
}