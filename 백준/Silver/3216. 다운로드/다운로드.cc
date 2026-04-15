#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n, d, v;
    cin >> n;
    
    cin >> d >> v;
    int answer=v;
    int diff=d;
    
    for (int i=0; i<n-1; i++) {
        cin >> d >> v;
        if (diff>=v) {
            diff-=v;
        } else {
            answer+= v-diff;
            diff=0;
        }
        diff+=d;
    }

    cout << answer;
    return 0;
}