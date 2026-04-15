#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m, k;
    cin >> n >> m;

    int waiting[1000];
    for (int i=0; i<n; i++) {
        cin >> waiting[i];
    }

    bool friends[1000]{};
    for (int i=0; i<m; i++) {
        cin >> k;
        friends[k]=1;
    }

    int answer=0;
    for (int i=0; i<m; i++) {
        if (!friends[waiting[i]]) {
            answer++;
        }
    }

    cout << answer;
    return 0;
}