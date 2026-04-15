#include <iostream>
#include <vector>
using namespace std;

void solve() {
    int k, m, p;
    cin >> k >> m >> p;

    vector<vector<int>> kang(m+1, vector<int>());
    vector<int> deg(m+1,0);

    int a, b; // a->b
    for (int i=0; i<p; i++) {
        cin >> a >> b;
        kang[a].push_back(b);
        deg[b]++;
    }

    vector<int> answer(m+1,0);
    vector<pair<int,int>> mul(m+1,{0,0});
    vector<int> st;
    for (int i=1; i<m+1; i++) {
        if (deg[i]==0) {
            st.push_back(i);
            answer[i]=1;
        }
    }

    vector<int> nxt_st;
    do {
        while (!st.empty()) {
            a=st.back();
            for (auto k : kang[a]) {
                deg[k]--;
                if (mul[k].first<answer[a]) {
                    mul[k]={answer[a],1};
                } else if (mul[k].first==answer[a]) {
                    mul[k].second++;
                }
                if (deg[k]==0) {
                    answer[k]=mul[k].second>=2?mul[k].first+1:mul[k].first;
                    nxt_st.push_back(k);
                }
            }
            st.pop_back();
        }
        st=nxt_st;
        nxt_st={};
    } while (!st.empty());

    cout << k << " " << answer[m] << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int tc;
    cin >> tc;
    for (int i=0; i<tc; i++) {
        solve();
    }
    return 0;
}