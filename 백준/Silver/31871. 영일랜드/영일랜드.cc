#include <iostream>
#include <vector>
using namespace std;

struct State {
    const int n;
    const vector<vector<long long>>& graph;
    vector<bool>& visited;
};

long long dfs(State& s, long long cost, int from, int cnt) {
    if (cnt==s.n) {
        if (s.graph[from][0]==-1) {
            return -1;
        }

        return cost+s.graph[from][0];
    }

    long long tmp=-1;
    for (int i=1; i<s.n+1; i++) {
        if (!s.visited[i] && s.graph[from][i]!=-1) {
            s.visited[i]=1;
            tmp=max(tmp,dfs(s,cost+s.graph[from][i],i,cnt+1));
            s.visited[i]=0;
        }
    }
    return tmp;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n, m, u, v;
    long long d;
    cin >> n >> m;

    vector<vector<long long>> graph(n+1,vector<long long>(n+1,-1));
    for (int i=0; i<m; i++) {
        cin >> u >> v >> d;
        graph[u][v]=max(graph[u][v],d);
    }

    long long answer=-1;
    // 0->i n=9

    vector<bool> visited(n+1,0);
    State s={n, graph, visited};
    for (int i=1; i<s.n+1; i++) {
        if (graph[0][i]==-1) {
            continue;
        }
        
        s.visited[i]=1;
        answer=max(answer,dfs(s,s.graph[0][i],i,1));
        s.visited[i]=0;
    }

    cout << answer << "\n";
    return 0;
}