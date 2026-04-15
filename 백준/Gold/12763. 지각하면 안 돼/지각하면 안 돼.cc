#include <iostream>
#include <queue>
#include <vector>
#include <tuple>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, t, m, l;
    cin >> n >> t >> m >> l;

    // init
    vector<vector<tuple<int,int,int>>> graph(n+1,vector<tuple<int,int,int>>());
    int v, nv, time, money;
    for (int i=0; i<l; i++) {
        cin >> v >> nv >> time >> money;
        graph[v].push_back({nv,time,money});
        graph[nv].push_back({v,time,money});
    }

    // dijk init 1->5
    auto cmp=[](auto a, auto b){return get<0>(a)>get<0>(b);};
    priority_queue<tuple<int,int,int>,vector<tuple<int,int,int>>,decltype(cmp)> pq(cmp);
    // money, v, time 최소 지출 찾기
    vector<vector<int>> visited(n+1,vector<int>(t+1,m+1));
    // visited[v][time]=money
    for (int i=0;i<t+1;i++) {
        visited[0][i]=0;
    }
    pq.push({0,1,0});

    // dijk
    while (!pq.empty()) {
        tie(money,v,time)=pq.top();pq.pop();
        if (visited[v][time]<money) continue;
        for (auto k : graph[v]) {
            auto [nv,nt,nm]=k;
            if (time+nt<=t && visited[nv][time+nt]>money+nm) {
                visited[nv][time+nt]=money+nm;
                pq.push({nm+money,nv,nt+time});
            }
        }
    }

    // find ans && print
    int answer=m+1;
    for (int i=0; i<=t; i++) {
        answer=min(answer,visited[n][i]);
    }

    if (answer!=m+1) {
        cout << answer;
    } else {
        cout << -1;
    }

    return 0;
}