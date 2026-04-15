#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    // 1 3 7 9  2 4v 5 6v 8v 10v
    // 1 1
    // 3 111
    // 7 111111
    // 11 11
    // 21 111111
    // 37 111
    // 101 1111

    // 11 3 8
    // 81 3 27 중국인의 나머지 어쩌고?

    int n, ans=0;
    cin >> n;
    if (n%2==0||n%5==0){
        ans=-1;
    } else {
        int k=0;
        do {
            k=(k*10+1)%n;
            ans++;
        } while (k!=0);
    }
    cout << ans;
    return 0;
}