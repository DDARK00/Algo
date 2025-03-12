#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <tuple>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, x, y, z;
    cin >> n;
    vector<vector<pair<int, int>>> graph(n);
    pair<int, int> xar[n], yar[n], zar[n];
    for (int i=0;i<n;i++){
        cin >> x >> y >> z;
        xar[i] = {x, i};
        yar[i] = {y, i};
        zar[i] = {z, i}; // w, v
    }
    sort(xar, xar+n);
    sort(yar, yar+n);
    sort(zar, zar+n);

    // n 100000*3
    int v1, v2, v3, nv1, nv2, nv3, nx, ny, nz;
    for (int i=0;i<n-1;i++){
        // w, v
        tie(x, v1) = xar[i];
        tie(nx, nv1) = xar[i+1];
        graph[v1].push_back({abs(x-nx), nv1});
        graph[nv1].push_back({abs(x-nx), v1});

        tie(y, v2) = yar[i];
        tie(ny, nv2) = yar[i+1];
        graph[v2].push_back({abs(y-ny), nv2});
        graph[nv2].push_back({abs(y-ny), v2});

        tie(z, v3) = zar[i];
        tie(nz, nv3) = zar[i+1];
        graph[v3].push_back({abs(z-nz), nv3});
        graph[nv3].push_back({abs(z-nz), v3});
    }

    // prim
    auto cmp = [](auto a, auto b){return a.first>b.first;};
    priority_queue<pair<int,int>, vector<pair<int, int>>, decltype(cmp)> pq(cmp);

    int ans =0;
    bool visited[n]{};
    pq.push({0,0});

    int v, w, nv, nw, end;
    end = 0;
    while(!pq.empty()){
        tie(w, v) = pq.top();
        pq.pop();
        if(visited[v])continue;
        visited[v]=true;
        ans+=w;
        end+=1;
        if(end==n)break;
        for(auto k: graph[v]){
            tie(nw, nv) = k;
            if(visited[nv])continue;
            pq.push(pair(nw, nv));
        }
    }
    cout << ans;
    return 0;
}