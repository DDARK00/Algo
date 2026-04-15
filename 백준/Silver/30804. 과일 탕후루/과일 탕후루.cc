#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    queue<int> q;
    int chk[10]{};
    int cnt=0, ans=0, temp;
    for (int i=0; i<n; i++) {
        cin >> temp;
        if (chk[temp] == 0) {
            cnt+=1;
        }
            chk[temp]+=1;
            q.push(temp);

        while(cnt>2){
            temp = q.front();
            q.pop();
            chk[temp]-=1;
            if(chk[temp]==0){
                cnt-=1;
            }
        }
        ans = max(ans, (int)q.size());
    }
    cout << ans;
    return 0;
}