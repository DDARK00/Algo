#include <iostream>
#include <queue>
#include <tuple>
#include <unordered_map>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, k, v, c;
    cin >> n >> k;
    unordered_map<int,bool> visited;
    queue<pair<int,int>> q;
    for (int i=0; i<n; i++) {
        cin >> v;
        visited[v]=1;
        q.push({v,0});
    }

    long long answer=0;
    while (!q.empty()){
        tie(v, c)=q.front();q.pop();
        for (int i=-1; i<2; i+=2) {
            if (visited[v+i]) continue;
            visited[v+i]=1;
            k-=1;
            answer+=c+1;
            if (k==0) {
                cout << answer;
                return 0;
            }
            q.push({v+i,c+1});
        }
    }
    return 0;
}