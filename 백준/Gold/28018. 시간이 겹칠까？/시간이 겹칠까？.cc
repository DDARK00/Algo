#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<pair<int, int>> datas;
vector<int> answer(1000001,0);
vector<int> table(1000001,0);

void solve(int n){
    int in_out, time;
    auto cmp=[](auto a, auto b){return a.second<b.second;};
    sort(datas.begin(),datas.end(),cmp);
    for (auto k : datas) {
        in_out=k.first;
        time=k.second;
        table[time] += in_out;
    }

    int pre_sum=0;
    for (int i=0; i<1000001; i++) {
        pre_sum+=table[i];
        answer[i]=pre_sum;
    }
}

void print(int t){
    cout << answer[t] << "\n";
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    // init
    int n, s, e;
    cin >> n;
    for (int i=0; i<n; i++) {
        cin >> s >> e;
        datas.push_back({1,s}); // in
        datas.push_back({-1,e+1}); //out
    }

    // solve
    solve(n);

    // cout
    int q, t;
    cin >> q;
    for (int i=0; i<q; i++) {
        cin >> t;
        print(t);
    }
    return 0;
}