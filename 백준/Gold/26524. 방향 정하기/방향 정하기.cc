#include <iostream>
using namespace std;

const long long MOD=1000000000+7;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n; // 100만
    cin >> n;
    // 사이클x -> DAG 위상 순서
    // 2 2 ab ba
    // 3 6 abc acb bac bca cab cba
    // 4 8

    long long answer=1;
    for (int i=2; i<n+1; i++) {
        answer*=i;
        answer%=MOD;
    }

    cout << answer;
    return 0;
}