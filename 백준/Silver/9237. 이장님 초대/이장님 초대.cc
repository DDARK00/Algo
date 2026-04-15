#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    cin >> n;
    int arr[100001];
    for (int i=0; i<n; i++) {
        cin >> arr[i];
    }
    sort(arr,arr+n,greater<int>());

    int answer=0;
    for (int i=0; i<n; i++) {
        answer=max(answer,arr[i]+i+2);
    }

    cout << answer;
    return 0;
}