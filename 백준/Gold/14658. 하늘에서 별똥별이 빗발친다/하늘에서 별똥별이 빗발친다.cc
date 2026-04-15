#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n, m, l, k;
    cin >> n >> m >> l >> k;

    int x, y, answer=0;
    vector<pair<int,int>> star;
    for (int i=0; i<k; i++) {
        cin >> x >> y;
        star.push_back({x,y});
    }

    for (auto p : star) { // 100*100*100
        auto [px, py]=p;
        for (auto q : star) {
            auto [qx, qy]=q;
            int lx=min(px,qx), ly=min(py,qy);

            int tmp=0;
            for (auto r : star) {
                auto [tx, ty]=r;
                if (lx<=tx && lx+l>=tx && ly<=ty && ly+l>=ty) {
                    tmp++;
                }
            }
            answer=max(tmp,answer);
        }
    }

    cout << k-answer;
    return 0;
}