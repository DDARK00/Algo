#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    string a, b;
    cin >> a >> b;
    int n=a.size();

    int i=n-1, j=n-1, answer=n;
    int chk[26]{};
    for (int k=0; k<n; k++) {
        chk[a[k]-'A']++;
    }

    for (; i>-1; i--) {
        if (a[i]==b[j]) {
            answer--;
            j--;
            chk[a[i]-'A']--;
        }
    }

    for (; j>-1; j--) {
        chk[b[j]-'A']--;
    }

    for (auto k : chk) {
        if (k>0) {
            cout << -1;
            return 0;
        }
    }

    cout << answer;
    return 0;
}