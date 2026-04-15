#include <iostream>
#include <cmath>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    // 5
    // 3 1 -2 4 -5
    
    // 3 -6 12 -15 -> -6
    // -2 4 -5 -> -3
    // -8 10 -> 2
    // -20
    int n;
    cin >> n;
    int arr[n];
    long long ans=0, temp, b=0;
    for (int i=0; i<n; i++){
        cin >> arr[i];
        b+=arr[i];
    }
    for (int i=0; i<n; i++) {
        b -= arr[i];
        ans += b* arr[i];
    }
    cout << ans;
    return 0;
}