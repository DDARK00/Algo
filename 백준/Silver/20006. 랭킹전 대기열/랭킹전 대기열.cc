#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int p, m, l;
    cin >> p >> m;

    string n;
    vector<vector<pair<int,string>>> room;
    for (int i=0; i<p; i++) {
        bool join=false;
        cin >> l >> n;
        for (int i=0; i<room.size(); i++) {
            if (room[i].size()==m||room[i][0].first+10<l || room[i][0].first-10>l) {
                continue;
            }
            join=true;
            room[i].push_back({l,n});
            break;
        }
        if (!join) {
            vector<pair<int,string>> new_room={{l,n}};
            room.push_back(new_room);
        }
    }

    auto cmp = [](auto a, auto b){return a.second<b.second;};
    for (int i=0; i<room.size(); i++) {
        if (room[i].size()==m) {
            cout << "Started!" << "\n";
        }else{
            cout << "Waiting!" << "\n";
        }
        sort(room[i].begin(),room[i].end(),cmp);
        for (auto k : room[i]) {
            cout << k.first << " " << k.second << "\n";
        }
    }
    return 0;
}