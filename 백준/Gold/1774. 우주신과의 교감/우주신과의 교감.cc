#include <iostream>
#include <queue>
#include <vector>
#include <tuple>
#include <cmath>

using namespace std;


const int MAX_SIZE = 1001;
pair<int, int> god[MAX_SIZE];
vector<pair<double,int>> graph[MAX_SIZE];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int n, m;
    cin >> n >> m;

    for (int i=1; i<n+1; i++) {
        cin >> god[i].first;
        cin >> god[i].second;
    }
    double temp;
    for (int i=1; i<n+1; i++) {
        for (int j=i+1; j<n+1; j++) {
            temp = sqrt(pow(god[i].first-god[j].first,2)+pow(god[i].second-god[j].second,2));
            graph[i].push_back({temp, j});
            graph[j].push_back({temp, i});
        }
    }
    int a, b;
    for (int i=0; i<m; i++) {
        cin >> a >> b;
        graph[a].push_back({0,b});
        graph[b].push_back({0,a});
    }
    auto cmp = [](auto a, auto b){return a.first>b.first;};
    priority_queue<pair<double, int>, vector<pair<double,int>>, decltype(cmp)> pq(cmp);

    bool visited[n+1]{};
    pq.push({0,1}); // w, v
    double ans = 0;

    double w;
    int v;
    while(!pq.empty()){
        tie(w, v) = pq.top();
        pq.pop();

        if(visited[v]) continue;
        visited[v] = true;
        ans += w;
        for (auto k : graph[v]) {
            // k.first; // w
            // k.second; // v
            if(!visited[k.second]){
                pq.push(k);
            }
        }
    }
    cout << fixed;
    cout.precision(2);
    cout << ans ;
    return 0;
}