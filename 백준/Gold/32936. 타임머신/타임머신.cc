#include <iostream>
#include <queue>
#include <vector>
using namespace std;

const int MAX=1050000000;
void bfs(int st, vector<vector<int>> graph, vector<int>&dist){
    queue<int> q;
    q.push(st);
    dist[st]=0;

    while (!q.empty()){
        auto v=q.front();q.pop();
        for (auto nv : graph[v]) {
            if (dist[nv]>dist[v]+1){
                dist[nv]=dist[v]+1;
                q.push(nv);
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    //init
    int n, m, a, b, c;
    cin >> n >> m >> a >> b >> c;

    // 유향
    int u, v, answer;
    vector<vector<int>> graph(n+1, vector<int>());
    for (int i=0; i<m; i++) {
        cin >> u >> v;
        graph[u].push_back(v);
    }

    // 1. 1-> a, b->n
    // 2. 1->a->b->a...
    // 3. 1->n
    // 4. 1->n->a->b...

    // bfs 1->n
    vector<int> dist(n+1,MAX); // v=200000
    bfs(1,graph,dist);
    answer=dist[n];
    int one_to_n=dist[n];
    int one_to_a=dist[a];

    // bfs b->n
    dist.assign(n+1,MAX);
    bfs(b,graph,dist);
    int b_to_n=dist[n];
    if (dist[a]<c && one_to_a!=MAX && dist[n]!=MAX){
        cout << "-inf";
        return 0;
    }
    answer=min(answer,one_to_a+dist[n]-c);

    // bfs n->a
    dist.assign(n+1,MAX);
    bfs(n,graph,dist);
    int n_to_a=dist[a];
    if (answer!=MAX && n_to_a+b_to_n<c) {
        cout << "-inf";
        return 0;
    }

    if (answer==MAX){
        cout << "x";
    }else{
        cout << answer;
    }
    return 0;
}