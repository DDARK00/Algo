#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N, S, D, F, B, K;
    cin >> N >> S >> D >> F >> B >> K;

    vector<int> visited(100001, -1);
    int tmp;
    for (int i=0; i<K; i++) {
        cin >> tmp;
        visited[tmp]=-2;
    }

    // -1기본 -2 경찰서 양수는 횟수
    queue<int> q;
    q.push(S);
    visited[S]=0;

    int d[2]={F, -B};
    while (!q.empty()) {
        tmp=q.front();q.pop();
        for (auto k : d) {
            if (tmp+k>0 && tmp+k<=N && visited[tmp+k]==-1){
                q.push(tmp+k);
                visited[tmp+k]=visited[tmp]+1;
            }
        }
    }

    if (visited[D]<0) {
            cout << "BUG FOUND";
    }else {
            cout << visited[D];
    }
    return 0;
}