#include <iostream>
#include <queue>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    string s;
    cin >> s;

    if (s[s.size()-1]!='5' && s[s.size()-1]!='0') {
        cout << -1;
        return 0;
    }

    s.erase(s.size()-2,1);
    long long n=stoll(s);
    n/=5;
    // 9 7 4.5 2 90 70 45 20 5
    int delta[]={18,14,9,-4};

    queue<int> q;
    q.push(0);
    int visited[2521]{}; // 18*14*9
    visited[0]=1;
    while (!q.empty()) {
        auto v=q.front();q.pop();
        for (auto d : delta) {
            auto nv=v+d;
            if (0<=nv&&nv<2520&&!visited[nv]) {
                visited[nv]=visited[v]+1;
                q.push(nv);
            }
        }
    }
    long long ans=0;
    if (n>2500) {
        ans+=(n-2500)/18;
        n-=(ans*18);
    }
    cout <<ans+visited[n]-1;
    return 0;
}