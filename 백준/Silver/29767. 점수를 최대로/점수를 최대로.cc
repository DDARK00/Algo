#include <iostream>
#include <algorithm>
 
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
 
    int n, k;
    long long s;
    cin >> n >> k;
    int score[n];
    long long ans[n];
    s=0;
    for (int i=0; i<n; i++) {
        cin >> score[i];
        s+=score[i];
        ans[i] = s;
    }
    sort(ans, ans+n, greater<long long>());
    s=0;
    for(int i=0;i<k;i++){
        s+=ans[i];
    }
    cout << s;
    return 0;
}
// 어오 자료형