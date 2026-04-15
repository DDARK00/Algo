#include <iostream>
using namespace std;

int board[9][9]{};

void ans(){
    for (int i=0; i<9; i++) {
        for (int j=0; j<9; j++) {
            cout << board[i][j] << " ";
        }
        cout << "\n";
    }
}
bool check_x[9][10]{};
bool check_y[9][10]{};
bool check_c[9][10]{};


bool dfs(int k){
    if(k == 81){
        return true;
    }
    
    int x, y, c;
    x = k/9;
    y = k%9;
    c = y/3 + x/3 * 3;
    if(board[x][y] == 0){
        for (int target = 1; target<10; target++) {
            if(check_x[x][target] == false and check_y[y][target] == false and check_c[c][target] == false){
                board[x][y] = target;
                check_x[x][target] = true;
                check_y[y][target] = true;
                check_c[c][target] = true;
                bool tf = dfs(k+1);
                if(!tf){
                    board[x][y] = 0;
                    check_x[x][target] = false;
                    check_y[y][target] = false;
                    check_c[c][target] = false;
                }else{
                    return true;
                }
            }
        }
        return false;
    }else{
        return dfs(k+1);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    for (int i=0; i<9; i++) {
        int temp;
        for (int j=0; j<9; j++) {
            cin >> temp;
            board[i][j] = temp;
            if(temp != 0){
                int c = j/3 + i/3 * 3;
                check_x[i][temp]=true;
                check_y[j][temp]=true;
                check_c[c][temp]=true;
            }
        }
    }
    dfs(0);
    ans();
    return 0;
}