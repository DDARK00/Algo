#include <iostream>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    cin >> n;
    int answer = 0, temp;
    
    for (int i=0; i<n; i++) {
        cin >> temp;
        answer ^= temp^i;
    }
    cout << answer;
    return 0;
}