#include <iostream>
#include <vector>
using namespace std;

int n, m;

int solve(int ans[15], int real_cnt, int need_cnt, vector<int> origin){
    if(real_cnt != need_cnt)return 1e9;

    int answer=0, temp;
    for (int i=0; i<n; i++) {
        // cout << ans[i] << " ";
        if (ans[i] != origin[i]) {
            temp=1;
            while(ans[i] != origin[i+temp]){
                temp++;
            }
            answer+= temp;
            origin[i+temp]= (origin[i+temp]+1)%2;
        }
    }
    return answer;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> n >> m;
    int cnt[2] ={0, 0};
    vector<int> origin(15);
    
    for (int i=0; i<n; i++) {
        cin >> origin[i];
        cnt[origin[i]]++;
    }

    int ans1[15], ans2[15];
    int temp, idx=0, odd_cnt=0;
    
    for (int i=0; i<m; i++) {
        cin >> temp;
        for (int j=0; j<temp; j++) {
            ans1[idx] = i%2; // 0 1 0 1
            ans2[idx] = (i+1)%2; // 1 0 1 0
            idx++;
        }
        if (i%2)odd_cnt+=temp; // 홀수번째 수
    }
    // if cnt[1]실제 1의개수 != ans1의 odd_cnt, ans2의 n-odd_cnt return 1e9
    cout << min(solve(ans1, cnt[1], odd_cnt, origin), solve(ans2,cnt[0], odd_cnt, origin));
    return 0;
}