#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    long long n, m, k, x, y;
    cin >> n >> m >> k >> x >> y;

    // n개의 역 중 m개의 역에 급행
    // k분 소요 -> x일반 y급행
    long long a, b;
    vector<long long> arr;
    for (int i=0; i<n; i++) {
        cin >> a >> b;
        arr.push_back(y*b-x*a);
    }

    sort(arr.begin(),arr.end(),greater<long long>());

    k=k*(x+y);
    for (int i=0; i<m; i++) {
        k-=arr[i];
    }

    cout << k;
    return 0;
}