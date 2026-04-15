#include <iostream>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n, temp;
    cin >> n;
    int want[1000001]{};
    for (int i=0; i<n; i++) {
        cin >> temp;
        want[temp]++;
    }
    for (int i=0; i<n; i++) {
        cin >> temp;
        want[temp]--;
    }

    int answer=0;
    for (int i=0; i<1000001; i++) {
        answer += max(0,want[i]);
    }
    cout << answer;
    return 0;
}