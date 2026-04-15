#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    cin >> n;

    long long answer=0, high=0, temp;
    for (int i=0; i<n; i++) {
        cin >> temp;
        answer+=temp;
        high=max(high,temp);
    }

    answer += high*(n-2);
    cout << answer;
    return 0;
}