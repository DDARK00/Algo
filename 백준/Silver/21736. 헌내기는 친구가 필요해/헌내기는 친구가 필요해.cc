#include <iostream>
#include <vector>
#include <tuple>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n, m;
    cin >> n >> m;
    vector<vector<char>> campus(n,vector<char>(m));
    int x, y;
    for (int i=0; i<n; i++) {
        for (int j=0; j<m; j++) {
            cin >> campus[i][j];
            if (campus[i][j]=='I') {
                x=i;
                y=j;
            }
        }
    }

    vector<pair<int,int>> st;
    st.push_back({x,y});
    campus[x][y]='X';
    vector<pair<int,int>> delta= {{1,0},{0,1},{-1,0},{0,-1}};
    int answer=0;
    while (!st.empty()){
        tie(x,y)=st.back();
        st.pop_back();
        for (auto k :delta) {
            auto [dx,dy]=k;
            if (0>x+dx||n==x+dx||0>y+dy||m==y+dy) {
                continue;
            }
            if (campus[x+dx][y+dy]=='X') {
                continue;
            }
            if (campus[x+dx][y+dy]=='P') {
                answer++;
            }
            campus[x+dx][y+dy]='X';
            st.push_back({x+dx,y+dy});
        }
    }

    if (answer==0){
        cout << "TT";
    }else{
        cout << answer;
    }
    return 0;
}