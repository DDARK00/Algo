#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>
using namespace std;

string vc_to_str(vector<char> puzzle){
    string rst="";
    for (auto c : puzzle) {
        rst+=c;
    }
    return rst;
}

int get_zero_pos(string puzzle){
    int pos;
    for (int i=0; i<9; i++) {
        if (puzzle[i]=='0') {
            pos=i;
            break;
        }
    }
    return pos;
}

void solve(vector<char> puzzle, int st){
    queue<string> q;
    unordered_map<string,int> visited;

    // 0 1 2
    // 3 4 5
    // 6 7 8
    vector<vector<int>> nxt={
    {1,3},{0,2,4},{1,5},{0,4,6},{1,3,5,7},{2,4,8},{3,7},{4,6,8},{5,7}
    };
    string v=vc_to_str(puzzle), nv;
    visited[v]=1; // v=cnt+1
    q.push(v);
    // bfs
    int pos;
    while (!q.empty()){
        v=q.front();
        q.pop();
        pos=get_zero_pos(v);
        // cout << pos << "\n";
        for (auto swap : nxt[pos]) {
            nv=v;
            nv[pos]=nv[swap];
            nv[swap]='0';
            // cout << nv << "\n";
            if (visited[nv]==0){
                visited[nv]=visited[v]+1;
                q.push(nv);
            }
        }
    }
    cout << visited["123456780"]-1;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    vector<char> puzzle(9);
    int st;
    for (int i=0; i<9; i++) {
        cin >> puzzle[i];
        if (puzzle[i]=='0') {
            st=i;
        }
    }
    solve(puzzle, st);
    return 0;
}