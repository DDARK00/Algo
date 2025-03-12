#include <iostream>
using namespace std;

void dfs(int k,int group, int cnt);
int visited[100001][2];
int arr[100001];
int ans;

void solve(){
    int n;
    ans = 0;
    cin >> n;
    // init
    for (int i=0; i<n; i++) {
        int temp;
        cin >> temp;
        // one team
        if (temp == i+1){
            ans +=1;
            // group, number
            visited[i+1][0] = -1;
            visited[i+1][1] = i+1;
        }else{
            arr[i+1] = temp;
            visited[i+1][0] = 0;
            visited[i+1][1] = 0;
        }
    }

    int group = 1;
    // dfs
    for (int i=1; i<n; i++) {
        if(!visited[i][0]){
            visited[i][0] = group;
            visited[i][1] = 0;
            dfs(i, group, 1);
            group+=1;
        }
    }
    cout << n-ans << "\n";
}

void dfs(int k, int group, int cnt){
    int nxt = arr[k];
    // same group and same depth
    if(visited[nxt][0] == 0){
        // not visited
        visited[nxt][0] = group;
        visited[nxt][1] = cnt;
        dfs(nxt, group, cnt+1);
    }else{
        // visited
        // same group and cnt
        if(visited[nxt][0] == group){
            ans += cnt - visited[nxt][1];
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int tc;
    cin >> tc;
    for (int i=0; i<tc; i++) {
        solve();
    }
    return 0;
}