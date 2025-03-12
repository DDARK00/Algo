#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int tc;
    cin >> tc;
    for (int i=0; i<tc; i++) {
        int a, b;
        cin >> a >> b;
        cout << "Case "<< i+1 <<": " << a+b << "\n";
    }
    return 0;
}