#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int q;
    cin >> q;

    // 행동stack 결과 stack
    vector<int> st;
    vector<pair<int,int>> p_st; // 1in 2out
    int i, j;
    for (int k=0; k<q; k++) {
        cin >> i;
        switch (i) {
            case 1:
                cin >> j;
                st.push_back(j);
                p_st.push_back({1,j});
                break;
            case 2:
                p_st.push_back({2,st.back()});
                st.pop_back();
                break;
            case 3:
                cin >> j;
                for (int l=0; l<j; l++) {
                    // 1 out 2 in
                    auto [o, t]=p_st.back();
                    p_st.pop_back();
                    if (o==2) {
                        st.push_back(t);
                    } else {
                        st.pop_back();
                    }
                }
                break;
            case 4:
                cout << st.size() << "\n";
                break;
            case 5:
                if (st.empty()) {
                    cout << -1;
                } else {
                    cout << st.back();
                }
                cout << "\n";
                break;
        }
    }
    return 0;
}