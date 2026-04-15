#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    cin >> n >> m;
    int a, b, c;
    cin >> a >> b >> c;
    // 너비 너비 길이

    // 300 20 
    vector<vector<int>> park(n+1, vector<int>(m+1));
    for (int i=1; i<n+1; i++) {
        for (int j=1; j<m+1; j++) {
            cin >> park[i][j];
            park[i][j]+=park[i-1][j]+park[i][j-1]-park[i-1][j-1];
        }
    }

    int answer=100000000; // 300 300 150 150 150
    for (int i=0; i<n+1; i++) {
        for (int j=0; j<m+1; j++) {
            // case1 a * b+c
            if (i+a<=n && j+b+c<=m) {
                int campcar=park[i+a][j+b+c]-park[i+a][j]-park[i][j+b+c]+park[i][j];
                answer=min(answer,campcar);
            }

            // case2 a+b * c+a
            if (i+b+a<=n && j+a+c<=m) {
                int car=park[i+b+a][j+c+a]-park[i+b+a][j+c]-park[i+a][j+c+a]+park[i+a][j+c];
                int camp=park[i+a][j+c]-park[i+a][j]-park[i][j+c]+park[i][j];
                answer=min(answer,car+camp);
            }

            // case3 b+a * a+c
            if (i+a+c<=n && j+b+a<=m) {
                int car=park[i+a][j+b]-park[i+a][j]-park[i][j+b]+park[i][j];
                int camp=park[i+a+c][j+b+a]-park[i+a+c][j+b]-park[i+a][j+b+a]+park[i+a][j+b];
                answer=min(answer,car+camp);
            }

        }
    }
    //for (int i=0; i<n+1; i++){
    //    for (auto k : park[i]) {
    //        cout << k << " ";
    //    }
    //    cout << "\n";
    //}

    cout << answer;
    return 0;
}