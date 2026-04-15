#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int t, n, m;
    cin >> t >> m >> n;
    string t_name;
    int b_time;
    vector<pair<int,string>> tt;
    for (int i=0; i<t; i++) {
        cin >> t_name >> b_time;
        while (b_time != -1){
            tt.push_back({(b_time+60-m)%60,t_name});
            cin >> b_time; // 시간 이름
        }
    }
    auto cmp=[](auto a, auto b){return a.first<b.first;};
    sort(tt.begin(),tt.end(),cmp);
    n-=1;
    n%=tt.size();
    cout << tt[n].second;
    return 0;
}