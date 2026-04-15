#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

vector<int> member;
int n, m;
unordered_map<int, int> cache;
void solve(int k, int cnt, int sums) {
    if (k==m) {
        return;
    }
    if (cache.find(sums)!=cache.end() && cache[sums]<=cnt) {
        solve(k+1,cache[sums],sums);
        return;
    }
    cache[sums]=cnt;
    for (int i=k; i<m; i++) {
        solve(k+1,cnt+1,sums|member[i]);
        solve(k+1,cnt,sums);
    }
    return;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> n >> m;
    n= (1<<n)-1;

    for (int i=0; i<m; i++) {
        int cnt, num, bit=0;
        cin >> cnt;
        for (int j=0; j<cnt; j++) {
            cin >> num;
            bit += 1<<(num-1);
        }
        member.push_back(bit);
    }

    solve(0, 0, 0);
    int answer=-1;
    if (cache.find(n)!=cache.end()) {
        answer=cache[n];
    }

    cout << answer;
    return 0;
}