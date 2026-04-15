#include <iostream>
#include <vector>
using namespace std;

int n, k; // 캔종류 날짜
vector<int> cnt(5);
vector rang(4, vector<int> (5));
vector merry(4, vector<int> (5));

int answer=0;
void solve(int day, int tmp) {
    if (day==k) {
        answer=max(answer, tmp);
        return;
    }
    for (int i=0; i<n; i++) {
        if (cnt[i]==0) {
            continue;
        }
        cnt[i]--;
        tmp+=rang[day][i];
        for (int j=0; j<n; j++) {
            if (cnt[j]==0) {
                continue;
            }
            cnt[j]--;
            tmp+=merry[day][j];
            solve(day+1, tmp);
            tmp-=merry[day][j];
            cnt[j]++;
        }
        tmp-=rang[day][i];
        cnt[i]++;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    // init
    cin >> n >> k;
    for (int i=0; i<n; i++) {
        cin >> cnt[i];
    }
    for (int i=0; i<k; i++) {
        for (int j=0; j<n; j++) {
            cin >> rang[i][j];
        }
    }
    for (int i=0; i<k; i++) {
        for (int j=0; j<n; j++) {
            cin >> merry[i][j];
        }
    }

    // n=5 k=4 5^2 k
    solve(0, 0);

    cout << answer;
    return 0;
}