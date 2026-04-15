#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n, k;
    cin >> n >> k;

    int cats[5001];
    for (int i=0; i<n; i++) {
        cin >> cats[i];
    }
    sort(cats,cats+n);

    int l=0, r=n-1, answer=0;
    while (l<r) {
        if (cats[l]+cats[r] <=k) {
            answer++;
            l++;
            r--;
            continue;
        }
        if (cats[l]+cats[r]>k) {
            r--;
        } else {
            l++;
        }
    }

    cout << answer;
    return 0;
}