#include <iostream>
#include <unordered_map>
#include <queue>
#include <vector>
using namespace std;

int solve(vector<int> coins, int m){
    queue<int> q;
    q.push(0);

    int x; // value
    unordered_map<int,int> visited; // cnt
    visited[0]=1;
    while (!q.empty()){
        x=q.front();
        q.pop();
        if (x==m){
            return visited[m]-1;
        }
        for (auto coin : coins) {
            if (!visited[x+coin] && x+coin<20001 && x+coin>-20001) {
                visited[x+coin]=visited[x]+1;
                q.push(x+coin);
            }
        }
    }
    return -1;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n, m;
    cin >> n >> m;
    vector<int> coins(n);
    for (int i=0; i<n; i++) {
        cin >> coins[i];
    }

    cout << solve(coins, m);
    return 0;
}