#include <iostream>
#include <tuple>
#include <vector>
using namespace std;
 
char ar[30][30];
int n;
vector<tuple<int,int>> d= {{-1,0},{0,-1},{-1,-1},{1,-1}};

bool check(int x, int y){
    char target = ar[x][y];
    int dx, dy;
    for (int i=0; i<4; i++){
        tie(dx, dy)=d[i];
        for(int j=0; j<3;j++){
            if (0>x+dx*j || 0>y+dy*j || n==y+dy*j)break;
            // x, y cross up cross down
            if (ar[x+dx*j][y+dy*j]!=target)break;
            if (j==2) return true;
        }
    }
    return false;
}

void solve(){
    for (int i=n-1; i>=0; i--) {
        for (int j=n-1; j>=0; j--){
            if (ar[i][j] != '.'&&check(i, j)){
                cout << ar[i][j];
                return;
            }
        }
    }
    cout <<"ongoing";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cin>>n;
    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            cin >> ar[i][j];
        }
    }
    solve();
    return 0;
}