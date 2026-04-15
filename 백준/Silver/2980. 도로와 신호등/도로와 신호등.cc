#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n, l;
    cin >> n >> l;
    int d, r, g;

    long long answer=0;
    int pos=0;
    for (int i=0; i<n; i++) {
        cin >> d >> r >> g;
        if (pos<d) {
            answer+=d-pos;
            pos=d;
        }
        // r+g 사이클
        // g~r-1 초록불
        int now = answer%(r+g);
        if (now>r && now <r+g){
            continue;
        } else{
            answer += r-now;
        }
    }
    answer += l-pos;
    cout << answer;
    return 0;
}