#include <iostream>
#include <queue>
using namespace std;

int main() {
    int a,k;
    cin >> a >> k;
    int visited[1000001]{};

    queue<int> q;
    q.push(a);
    visited[a]=1;
    int v;
    while (!q.empty()) {
        v=q.front();q.pop();
        for (int d : {1,v}) {
            if (v+d<=k && visited[v+d]==0) {
                visited[v+d]=visited[v]+1;
                q.push(v+d);
            }
        }
    }
    cout << visited[k]-1;
    return 0;
}