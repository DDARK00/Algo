#include <iostream>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
    cin.tie(NULL);
    int tc, n;
    cin >> tc;

    for (int i=0;i<tc;i++) {
        cin >> n;
        cout << "YES" << "\n";
        // 2 3 5 7 11 13 17
        // 1 2 3 4 5 6 7
        for (int i=1;i<n+1;i++) {
            cout << i << " ";
        }
        cout << "\n";
    }

	return 0;
}