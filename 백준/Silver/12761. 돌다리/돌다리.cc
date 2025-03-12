#include <iostream>
#include <queue>
using namespace std;

bool visited[100001];

void bfs(int a, int b, int start, int end){
    queue<pair<int,int>> q;
    q.push({start,0});
    visited[start] = true;

    while(!q.empty()){
        int v=q.front().first;
        int cnt=q.front().second;
        if (v==end){
            cout<<cnt<<"\n";
            break;
        }
        q.pop();
        int d[8]={v+1,v-1,v+a,v-a,v+b,v-b,v*a,v*b};
        for(int i=0;i<8;i++){
            if(d[i]>=0 and d[i]<100001 and !visited[d[i]]){
                q.push({d[i],cnt+1});
                visited[d[i]]=true;
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int a, b, n, m;
    cin >> a >> b >> n >> m;
    bfs(a,b,n,m);
    return 0;
}