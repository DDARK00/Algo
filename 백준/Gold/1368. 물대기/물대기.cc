#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    cin >> n;

    auto cmp = [](pair<int, int>&a, pair<int, int>&b)->bool {return a.first>b.first;};
    priority_queue<pair<int, int>, vector<pair<int, int>>, decltype(cmp)> pq(cmp);
    vector<vector<pair<int,int>>> g(n);
    for(int i=0;i<n;i++){
        int w;
        cin >> w;
        pq.push(pair(w, i));
    }

    for (int i=0; i<n; i++) {
        for(int j=0; j<n; j++){
            int a;
            cin >> a;
            if(i==j)continue;
            g[i].push_back(pair(a, j));
        }
    }

    // prim?
    bool visited[n] = {};
    int cnt = 0;
    int ans = 0;
    while(!pq.empty() && cnt<n){
        int w = pq.top().first;
        int v = pq.top().second;
        pq.pop();
        if(!visited[v]){
            visited[v] = true;
            ans += w;
            for(auto k:g[v]){
                int nw = k.first;
                int nv = k.second;
                pq.push(pair(nw,nv));
            }
        }
    }

    cout << ans << "\n";
    return 0;
}