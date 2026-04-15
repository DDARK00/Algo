#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    long long almost_pibo[117];
    almost_pibo[1]=1;
    almost_pibo[2]=1;
    almost_pibo[3]=1;
    for (int i=4; i<117; i++) {
        almost_pibo[i]=almost_pibo[i-1]+almost_pibo[i-3];
    }
    cin >> n;
    cout << almost_pibo[n];
    return 0;
}