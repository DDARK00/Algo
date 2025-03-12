#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int a, b;

    cin >> a >> b;
    long long gcd = __gcd(a,b);
    long long ans = (long long)a*b/gcd;
    cout << ans;
	return 0;
}