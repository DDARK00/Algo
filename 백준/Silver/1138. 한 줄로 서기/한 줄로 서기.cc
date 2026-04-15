#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, temp, cnt, pos;
    cin >> n;
    vector<int> answer(n,n+1);
    for (int i=1; i<n+1; i++) {
        // 현재 키가 i일 때, 큰 사람이 왼쪽에 temp명
        // 앞에서부터 채우면
        cin >> temp;
        cnt=0;
        pos=0;
        for (int j=0; j<n; j++) {
            pos++;
            if (answer[j]>i) {
                cnt++;
                if (cnt==temp+1) {
                    pos--;
                    break;
                }
            }
        }
        answer[pos]=i;
        // cout << pos << " = " << i <<"\n";
    }

    for (auto k : answer) {
        cout << k << " ";
    }
    return 0;
}