#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int n, tmp;
    cin >> n;
    int answer=0;
    vector<int> vc(n);
    for (int i=0; i<n; i++) {
        cin >> tmp;
        vc[tmp-1]=i;
    }

    for (int i=0; i<n-1; i++) {
        if (vc[i]>vc[i+1]) {
            answer++;
        }
    }
    cout << answer;
    return 0;
}
//5
//3 5 2 4 1
//53142