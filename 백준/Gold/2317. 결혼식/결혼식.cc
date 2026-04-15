#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n, m;
    cin >> n >> m;

    int answer=0;
    // 5 3
    // 1900 1300 1500 // 1200 1600 // 600 200 -> 800

    // 1900 1600 1300 1200 1500 // 300 300 100 300 -> 100
    // 사자의 하락or상승 지나가는 길에 중간값 담그고
    // 최고 최저값만 반영

    // 인간의 최소 최대가 사자보다 작고 크고
    // 사자의 최소 최대가 중간에 있으면 차이값만큼 왕복?
    // 왕복하면 2배라서 맨 앞/ 맨 뒤와의 차이가 최소가 되는 경우가 존재

    vector<int> lion(m);
    int mn=2147483647, mx=-1, tmp;
    for (int i=0; i<m; i++) {
        cin >> lion[i];
    }

    int l_mn=lion[0], l_mx=lion[0];
    for (int i=1; i<m; i++) {
        answer+=abs(lion[i]-lion[i-1]);
        l_mn=min(l_mn,lion[i]);
        l_mx=max(l_mx,lion[i]);
    }

    for (int i=0; i<n-m; i++) {
        cin >> tmp;
        mn=min(mn,tmp);
        mx=max(mx,tmp);
    }

    if (mn<l_mn) {
        answer+=min(abs(mn-l_mn)*2,abs(min(lion[0],lion[m-1])-mn));
    }

    if (mx>l_mx) {
        answer+=min(abs(mx-l_mx)*2,abs(max(lion[0],lion[m-1])-mx));
    }

    cout << answer;
    return 0;
}