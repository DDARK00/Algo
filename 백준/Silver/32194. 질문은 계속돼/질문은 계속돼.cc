#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    cin >> n;

    int a, b, c, tf;
    int answer[200002];
    answer[0]=0;
    answer[1]=1; // 0아니오 1예
    for (int i=1; i<n+2; i++) {
        cin >> a >> b >> c;
        if (a==1) {
            tf=(answer[c]-answer[b-1])==(c-(b-1))?1:0;
        }else{
            tf=(answer[c]-answer[b-1])==0?1:0;
        }
        answer[i+1]=answer[i]+tf;
    }

    for (int i=2; i<n+2; i++) {
        cout << (answer[i]-answer[i-1]?"Yes":"No") << "\n";
    }
    return 0;
}