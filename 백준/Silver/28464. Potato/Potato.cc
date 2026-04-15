#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    cin >> n;

    int arr[200000];
    for (int i=0; i<n; i++) {
        cin >> arr[i];
    }
    sort(arr,arr+n);

    int x=0, y=0;
    for (int i=0; i<n/2; i++) {
        x+=arr[i];
    }
    for (int i=n/2; i<n; i++) {
        y+=arr[i];
    }

    cout <<  x << " " << y;
    return 0;
}