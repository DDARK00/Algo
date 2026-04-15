#include <iostream>
#include <tuple>
#include <queue>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int a, b, c;
    cin >> a >> b >> c;
    // 10 15 35 20 15 25 5 30 25 25 25 25
    if ((a+b+c)%3) {
        cout << 0;
        exit(0);
    }else if(a==b&&b==c){
        cout << 1;
        exit(0);
    }
    queue<tuple<int,int,int>> q;
    // 500 500 500
    bool visited[1500][1500]{};
    q.push({a,b,c});

    const int MAX_VAL=a+b+c;
    int x, y;
    while (!q.empty()){
        tie(a,b,c)=q.front();
        q.pop();
        for (auto k:vector<pair<int,int>>({{a,b},{a,c},{b,c}})){
            tie(x,y)=k;
            if (x==y) continue;
            if (x>y) swap(x,y);
            // x<y
            y-=x;
            x+=x;
            if (y<0) continue;
            if (visited[x][y])continue;
            
            visited[x][y]=1;
            q.push({x,y,MAX_VAL-x-y});
        }
    }
    cout << visited[MAX_VAL/3][MAX_VAL/3];
    return 0;
}