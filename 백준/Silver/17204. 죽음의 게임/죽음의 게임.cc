#include <iostream>
#include <queue>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n, k;
    cin >> n >> k;

    int fingers[150];
    for (int i=0; i<n; i++) {
        cin >> fingers[i];
    }

    queue<int> q;
    int visited[150]{};
    q.push(0);
    int answer=1;
    visited[0]=1;
    while (!q.empty()) {
        int v=q.front();q.pop();
        int nv=fingers[v];
        if (nv==k) {
            break;
        }

        if (visited[nv]) {
            answer=-1;
            break;
        }
        visited[nv]=1;
        answer++;
        q.push(nv);
    }
    cout << answer;
    return 0;
}