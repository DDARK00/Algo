#include <iostream>
#include <queue>
using namespace std;

int n;
int board[100][100]{};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> n; // 1<=N<=100

    // init
    string temp;
    cin >> temp;
    for (int i=0; i<n; i++) {
        board[0][i]=temp[i]-'0';
    }

    for (int i=1; i<n-1; i++) {
        cin >> temp;
        board[i][0] = temp[0]-'0';
        board[i][n-1] = temp[n-1]-'0';
    }

    if (n>1) {
        cin >> temp;
        for (int i=0; i<n; i++) {
            board[n-1][i] = temp[i]-'0';
        }
    }

    int ans=max(0,(n-4))*max(0,(n-4)); // center
    int cnt[] = {0,0,0,0};
    queue<int> uq({0,0,0});
    queue<int> dq({0,0,0});
    queue<int> lq({0,0,0});
    queue<int> rq({0,0,0});

    for (int i=0; i<n-2; i++) {
        cnt[0]-=uq.front();uq.pop();
        cnt[1]-=dq.front();dq.pop();
        cnt[2]-=lq.front();lq.pop();
        cnt[3]-=rq.front();rq.pop();

        // u
        if (cnt[0]==board[0][i]) {
            uq.push(0);
        }else{
            uq.push(1);
            cnt[0]++;
            ans++;
        }

        // d
        if (cnt[1]==board[n-1][i]) {
            dq.push(0);
        }else{
            dq.push(1);
            cnt[1]++;
            ans++;
        }

        // l
        if (cnt[2]==board[i][0]) {
            lq.push(0);
        }else{
            lq.push(1);
            cnt[2]++;
            ans++;
        }

        // r
        if (cnt[3]==board[i][n-1]) {
            rq.push(0);
        }else{
            rq.push(1);
            cnt[3]++;
            ans++;
        }
    }

    if (n==3){
        ans = min(1,ans);
    }else{
        ans = ans-board[0][0]-board[0][n-1]-board[n-1][0]-board[n-1][n-1];
    }
    cout << ans;
    return 0;
}