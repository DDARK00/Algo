#include <iostream>
using namespace std;

int n, k, b;
bool light[100001]{};
void solve(){
    // k개 유지
    int r=k;
    int answer;
    int now=0;
    for (int i=1; i<k+1; i++) {
        now+=light[i];
        answer=now;
    }
    for (int i=k+1; i<n+1; i++) {
        now+=light[i];
        now-=light[i-k];
        answer=min(answer,now);
    }

    cout << answer;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> n >> k >> b;
    int temp;
    for (int i=0; i<b; i++) {
        cin >> temp;
        light[temp]=1;
        // 1error 0ok
    }
    solve();
    return 0;
}