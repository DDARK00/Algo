#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    string start, temp;
    cin >> n >> start;
    vector<vector<string>> g(81);

    for (int i=0; i<n; i++) {
        cin >> temp;
        g[temp.size()].push_back(temp);
    }

    queue<string> q;
    q.push(start);
    string answer=start;
    while (!q.empty()){
        temp=q.front();
        q.pop();
        answer=temp;
        for (auto k : g[temp.size()+1]) {
            int cnt=0;
            for (int j=0; j<k.size(); j++) {
                if (j>cnt+1)break;
                if (k[j]==temp[cnt]) {
                    cnt++;
                }
            }
            if (cnt==temp.size()) {
                q.push(k);
            }
        }
    }

    cout << answer;
    return 0;
}