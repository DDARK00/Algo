#include <iostream>
#include <tuple>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n, m, a, b;
    cin >> n >> m;

    int deg[n]{};
    vector<vector<int>> graph(n);
    for(int i=0;i<m;i++){
        cin >> a >> b;
        deg[b-1]+=1;
        graph[a-1].push_back(b-1);
    }

    vector<pair<int,int>> st;
    int ans[n]{};
    for(int i=0;i<n;i++){
        if(deg[i]==0){
            st.push_back({i,1});
            ans[i]=1;
        }
    }

    int v, d;
    while (!st.empty()){
        tie(v, d) = st.back();
        st.pop_back();
        for(int nv: graph[v]){
            deg[nv]-=1;
            ans[nv]=max(ans[nv],d+1);
            if (deg[nv]==0){
                st.push_back({nv, ans[nv]});
            }
        }
    }
    for(int num: ans){
        cout << num << " ";
    }
    return 0;
}