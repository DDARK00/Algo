#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;
    int line1[n];
    int line2[n];
    line1[0]=0;
    line2[0]=0;
    for (int i=0; i<n; i++) {
        cin >> line1[i];
    }
    for (int i=0; i<n; i++) {
        cin >> line2[i];
    }

    long long a=max(line1[0],line1[0]+line2[0]), b=line1[0]+line2[0]; //　line1 line2
    long long tmp1, tmp2;

    // 직전, 대각선, 직전+상하
    for (int i=1; i<n; i++) {
        
        tmp1=max(a,b+line2[i]);
        tmp1=max(tmp1,a+line2[i])+line1[i];
        tmp2=max(b,a+line1[i]);
        tmp2=max(tmp2,b+line1[i])+line2[i];
        a=tmp1, b=tmp2;
        // cout << tmp1 << " " << tmp2<<"\n";
    }

    cout << b;
    return 0;
}