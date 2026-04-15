#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> graph={{7},{2,4},{1,3,5},{2,6},{1,5,7},{2,4,6,8},{3,5,9},{0,4,8},{5,7,9},{6,8}};
vector<vector<int>> answer(1001, vector<int>(10));

void solve(){
    for (int i=0; i<10; i++) {
        answer[1][i]=1;
    }
    for (int i=2; i<1001; i++) {
        for (int j=0; j<10; j++) {
            for (auto k: graph[j]) {
                answer[i][j]+=answer[i-1][k];
                answer[i][j]%=1234567;
            }
        }
    }
}

int print(int n){
    int k=0;
    for (int i=0; i<10; i++) {
        k+=answer[n][i];
        k%=1234567;
    }
    return k;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int tc, n;
    cin >> tc;
    solve();
    for (int i=0; i<tc; i++) {
        cin >> n;
        cout << print(n) << "\n";
    }
    return 0;
}