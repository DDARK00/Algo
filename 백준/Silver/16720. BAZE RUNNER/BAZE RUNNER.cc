#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    string temp;
    cin >> n;
    vector<int> maze;
    for (int i=0; i<n-2; i++) {
        cin >> temp;
        for (int j=0; j<4; j++) {
            if (temp[j]=='0') {
                maze.push_back(j);
                break;
            }
        }
    }
    // n=1000
    vector<int> cnt={0,0,0,0};
    for (int i=0; i<4; i++) {
        for (int j=0; j<n-2; j++) {
            // maze[j]를 i로 0 1 0 3
            cnt[i]+=min((i+4-maze[j])%4, (maze[j]+4-i)%4);
        }
    }
    int answer=5000;
    for (auto k : cnt) {
        answer=min(answer,k);
    }
    cout << answer+3+(n-1);
    return 0;
}