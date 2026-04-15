#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n, l, r;
    cin >> n >> l >> r;

    vector<vector<int>> country(n,vector<int>(n));
    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            cin >> country[i][j];
        }
    }

    queue<pair<int,int>> q;
    vector<vector<bool>> visited(n,vector<bool>(n,1));
    vector<pair<int,int>> delta={{1,0},{0,1},{-1,0},{0,-1}};
    int answer=0;

    bool flag=true;
    while (flag) {
        flag=false;

        for (int i=0; i<n; i++) {
            for (int j=0; j<n; j++) {
                if (visited[i][j]!=answer%2) {
                    visited[i][j]=answer%2;
                    q.push({i,j});
                }

                // 움직이는 도시들
                vector<pair<int,int>> entry;
                int cnt=0, sum=0;
                while (!q.empty()) {
                    auto [x,y]=q.front();q.pop();
                    cnt++;
                    sum+=country[x][y];
                    entry.push_back({x,y});

                    for (auto k : delta) {
                        auto[dx, dy]=k;
                        if (dx+x>=0 && dx+x<n && dy+y>=0 && dy+y<n && visited[dx+x][dy+y]!=answer%2) {
                            int diff=abs(country[dx+x][dy+y]-country[x][y]);
                            if (diff>=l && diff<=r) {
                                visited[dx+x][dy+y]=answer%2;
                                q.push({dx+x,dy+y});
                            }
                        }
                    }
                }
                if (cnt>1){
                    flag=true;
                    int pop=sum/cnt; // 편의상 소수점은 버린다.
                    for (auto k : entry) {
                        auto [x,y]=k;
                        country[x][y]=pop;
                    }
                }
            }
        }

        if (flag) {
            answer+=1;
        }
    }

    // for (int i=0; i<n; i++) {
    //     for (int j=0; j<n; j++) {
    //         cout << country[i][j] << " ";
    //     }
    //     cout << "\n";
    // }
    cout << answer;
    return 0;
}