#include <iostream>
#include <vector>
#include <queue>
using namespace std;

const long long INT_MAX = 10e15;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int n, m, k;
    cin >> n >> m >> k;
    vector<vector<pair<int,int>>> graph(n+1);
    int a, b, c;

    // graph init
    for (int i=0;i<m;i++){
        cin >> a >> b >> c;
        graph[a].push_back({c, b}); // w, v
        graph[b].push_back({c, a});
    }

    auto cmp=[](auto a,auto b){return a.first>b.first;};
    // dijk
    priority_queue<pair<long long,int>,vector<pair<long long,int>>,decltype(cmp)> pq(cmp);
    vector<long long> dist(n+1);
    for (int i=0; i<n+1; i++) {
        dist[i] = INT_MAX;
    }
    pq.push({0, 1}); // w, v
    dist[1] = 0;

    while (!pq.empty()){
        auto [w, v] = pq.top();pq.pop();
        if(dist[v]<w)continue;
        for (auto data : graph[v]) {
            auto [nw, nv] = data;
            if(dist[nv]>w+nw){
                pq.push({w+nw,nv});
                dist[nv] = w+nw;
            }
        }
    }

    long long x, ex, answer=INT_MAX;
    cin >> x;
    for (int i=0;i<x;i++){
        cin >> ex;
        long long cnt=dist[ex]/k;
        long long now_idx=cnt%x;
        if (now_idx==i){
            answer=min(answer,dist[ex]);
        }else if (now_idx<i){
            answer=min(answer,(cnt-now_idx+i)*k);
        }else{
            answer=min(answer,(cnt-now_idx+i+x)*k);
        }
    }
    cout << answer;
    return 0;
}