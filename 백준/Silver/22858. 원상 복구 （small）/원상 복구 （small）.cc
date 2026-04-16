#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    // 1000 10000 10000000
    int n, k;
    cin >> n >> k;

    int arr1[10001];
    int arr2[10001];
    int order[10001];
    for (int i=1; i<n+1; i++) {
        cin >> arr1[i];
    }

    for (int i=1; i<n+1; i++) {
        cin >> order[i];
    }

    for (int i=0; i<k; i++) {
        if (i%2){ // 2->1
            for (int j=1; j<n+1; j++) {
                arr1[order[j]]=arr2[j];
            }
        } else { // 1->2
            for (int j=1; j<n+1; j++) {
                arr2[order[j]]=arr1[j];
            }
        }
    }

    if (k%2) {
        for (int i=1; i<n+1; i++) {
            cout << arr2[i] << " ";
        }
    } else {
        for (int i=1; i<n+1; i++) {
            cout << arr1[i] << " ";
        }
    }
    return 0;
}