#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int x, y, m;
    cin >> x >> y >> m;

    int tmp;
    vector<int> mob;
    for (int i=0; i<x; i++) {
        cin >> tmp;
        mob.push_back(tmp);
    }

    vector<int> po;
    for (int i=0; i<y; i++) {
        cin >> tmp;
        po.push_back(tmp);
    }

    int kill_cnt=0, potion_cnt=0;
    vector<pair<int,int>> answer;
    int hp=m;
    while (kill_cnt<x) {
        while (hp<=(m/2) && potion_cnt<y) {
            hp+=po[potion_cnt];
            answer.push_back({1,potion_cnt+1});
            potion_cnt++;
        }

        if (hp<=mob[kill_cnt]) {
            cout << 0;
            return 0;
        }

        hp-=mob[kill_cnt];
        answer.push_back({-1,kill_cnt+1});
        kill_cnt++;
    }

    for (auto k : answer) {
        cout << k.first*k.second << "\n";
    }
    for (int i=potion_cnt; i<y; i++) {
        cout << i+1 << "\n";
    }
    return 0;
}