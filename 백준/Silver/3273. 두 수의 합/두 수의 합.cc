#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int n, x;
    cin >> n;
    int arr[100000];
    for (int i=0; i<n; i++) {
        cin >> arr[i];
    }
    sort(arr,arr+n);
    int l=0, r=n-1, answer=0;
    cin >> x;
    while (l<r){
        if (arr[l]+arr[r]==x){
            answer+=1;
            l++;
        }else if (arr[l]+arr[r]>x){
            r--;
        }else{
            l++;
        }
    }
    cout << answer;
    return 0;
}