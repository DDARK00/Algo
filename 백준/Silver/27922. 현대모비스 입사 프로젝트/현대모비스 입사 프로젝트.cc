#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, k;
    cin >> n >> k;

    int a, b, c;
    vector<int> ab;
    vector<int> ac;
    vector<int> bc;
    for (int i=0; i<n; i++) {
        cin >> a >> b >> c;
        // 1,2 1,3 2,3
        ab.push_back(a+b);
        ac.push_back(a+c);
        bc.push_back(b+c);
    }
    sort(ab.begin(),ab.end(),greater<int>());
    sort(ac.begin(),ac.end(),greater<int>());
    sort(bc.begin(),bc.end(),greater<int>());

    // 10000,100000
    int result[3]={0,0,0};
    for (int i=0; i<k; i++) {
        result[0]+=ab[i];
        result[1]+=ac[i];
        result[2]+=bc[i];
    }

    int answer=max(result[0],result[1]);
    answer=max(answer,result[2]);

    cout << answer;
    return 0;
}