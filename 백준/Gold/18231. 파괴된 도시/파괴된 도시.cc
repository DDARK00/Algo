#include <iostream>
#include <vector>
#include <map>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    cin >> n >> m;
    vector<vector<int>> graph(n+1, vector<int>());

    int u, v;
    for (int i=0; i<m; i++) {
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    int k, p;
    cin >> k;
    vector<int> destroyed_vector;
    map<int, int> chk_city;
    map<int, int> destroyed;
    for (int i=0; i<k; i++) {
        cin >> p;
        destroyed_vector.push_back(p);
        destroyed[p]=1;
    }

    // 파괴 -> 근처 마을 전부 파괴o -> 투하o
    // 파괴 -> 근처 마을중 파괴x -> 투하x -> 근처 마을중 투하 x -> -1
    // 파괴된 마을 전부o -> t

    for (auto p : destroyed_vector) {
        bool ok=true;
        for (auto v : graph[p]) {
            if (!destroyed[v]) {
                ok=false;
                break;
            }
        }
        if (ok) {
            chk_city[p]=1;
        }
    }

    bool valid=true;
    int answer=0;
    vector<int> bomber;
    for (auto v : destroyed_vector) {
        if (chk_city[v]) {
            answer++;
            bomber.push_back(v);
            continue;
        }

        bool flag=false;
        for (auto nv : graph[v]) {
            if (chk_city[nv]) {
                flag=true;
                break;
            }
        }

        if (!flag) {
            valid=false;
            break;
        }
    }

    if (valid) {
        cout << answer << "\n";
        for (auto k : bomber) {
            cout << k << " ";
        }
    } else {
        cout << -1;
    }
    return 0;
}