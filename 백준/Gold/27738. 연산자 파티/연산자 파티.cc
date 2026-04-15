#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    long long n;
    int a,b,c,d,e,f;
    cin >> n >> a >> b >> c >> d >> e >> f;
    long long x=0;
    for (long long i=n/f*f+1; i<n+1; i++) {
        if (i%a==0) {
            x+=i;
        }
        if (i%b==0) {
            x%=i;
        }
        if (i%c==0) {
            x&=i;
        }
        if (i%d==0) {
            x^=i;
        }
        if (i%e==0) {
            x|=i;
        }
    }
    cout << x;
    return 0;
}