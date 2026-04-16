#include <iostream>
#include <vector>
#include <queue>
#include <tuple>
using namespace std;
const int INF=1e9;

int n, m, k, l, p;
int s, e;

vector<bool> trap(10001,0);
vector<vector<vector<pair<int,int>>>> graph(2,vector<vector<pair<int,int>>>(10001, vector<pair<int,int>>()));
//type, v, nw nv
vector<vector<vector<int>>> dist(2, vector<vector<int>>(10001, vector<int>(11, INF)));
// type, v, press cnt 0~10

void dijk() {
    auto cmp=[](auto a, auto b){return get<0>(a)>get<0>(b);};
    priority_queue<tuple<int,int,int,int>,vector<tuple<int,int,int,int>>, decltype(cmp)> pq(cmp);

    pq.push({0,s,0,0}); // w, v, cnt, stable-reversed type
    dist[0][s][0]=0;

    while (!pq.empty()) {
        auto [w, v, c, t]=pq.top();pq.pop();
        if (c==p) {
            t^=1;
            c=0;
        }
        if (dist[t][v][c]<w) continue;
        // cout << v << " " << w << "\n";

        for (auto nxt : graph[t][v]) {
            auto [nw, nv]=nxt;
            if (dist[t][nv][c+trap[nv]]>w+nw) {
                pq.push({nw+w,nv,c+trap[nv],t});
                dist[t][nv][c+trap[nv]]=w+nw;
            }
        }
    }
}

void print() {
    int answer=INF;
    for (int i=0; i<2; i++) {
        for (int j=0; j<11; j++) {
            answer=min(answer,dist[i][e][j]);
        }
    }

    if (answer==INF) {
        cout << -1;
    } else {
        cout << answer;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    // init
    cin >> n >> m >> k >> l >> p;
    int v, nv, w;
    for (int i=0; i<k; i++) {
        cin >> v;
        trap[v]=1;
    }

    // mk_graph
    for (int i=0; i<m-l; i++) {
        cin >> v >> nv >> w;
        graph[0][v].push_back({w,nv}); // 일방통행 w, v
        graph[1][v].push_back({w,nv}); // 일방통행 w, v
    }

    for (int i=0; i<l; i++) {
        cin >> v >> nv >> w;
        graph[0][v].push_back({w,nv}); // 함정 w, v
        graph[1][nv].push_back({w,v}); // 함정 w, v swap
    }

    cin >> s >> e;
    // solve
    dijk();

    // cout
    print();
    return 0;
}
