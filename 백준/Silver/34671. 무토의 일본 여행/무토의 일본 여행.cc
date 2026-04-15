#include <iostream>
#include <vector>
#include <map>
using namespace std;

struct Data {
    bool ok=false;
    int value=1000000001;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m, q;
    cin >> n >> m >> q;

    vector<map<int,Data>> graph(n+1);
    int a, b, c;
    int s, e;
    for (int i=0; i<m; i++) {
        cin >> a >> b >> c;
        s=min(a,b);
        e=max(a,b);
        graph[s][e].value=min(graph[s][e].value,c);
        graph[s][e].ok=true;
    }

    for (int i=0; i<q; i++) {
        cin >> a >> b;
        s=min(a,b);
        e=max(a,b);
        if (!graph[s][e].ok) {
            cout << -1 << "\n";
        } else {
            cout << graph[s][e].value << "\n";
        }
    }
    return 0;
}