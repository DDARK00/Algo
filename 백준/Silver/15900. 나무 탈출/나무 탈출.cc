#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n, a, b;
    cin >> n;
    vector<vector<int>> graph(n+1, vector<int>());
    for (int i=0; i<n-1; i++) {
        cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    vector<int> st={1};
    int visited[n+1]{};
    visited[1]=1;

    int v, answer=0;
    while (!st.empty()) {
        v=st.back();
        st.pop_back();

        bool child=false;
        for (auto k : graph[v]) {
            if (!visited[k]) {
                child=true;
                visited[k]=visited[v]+1;
                st.push_back(k);
            }
        }
        if (!child) {
            answer+=visited[v]-1;
        }
    }

    if (answer%2) {
        cout << "Yes";
    } else {
        cout << "No";
    }
    return 0;
}