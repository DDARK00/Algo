#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n, m;
    cin >> n >> m;
    vector<vector<char>> board(n, vector<char>(m));
    for (int i=0; i<n; i++) {
        for (int j=0; j<m; j++) {
            cin >> board[i][j];
        }
    }
    vector<vector<pair<int,int>>> delta={{{1,0},{0,1},{1,-1}},{{1,0},{0,1},{1,1}}};
    int answer=0;
    for (int i=0; i<n; i++) {
        for (int j=0; j<m; j++) {
            for (auto k : delta[i%2]) {
                auto [dx, dy]=k;
                if (i+dx<n && i+dx>=0 && j+dy<m && j+dy>=0 && board[i][j]!=board[i+dx][j+dy]) {
                    answer++;
                }
            }
        }
    }
    cout << answer;
    return 0;
}