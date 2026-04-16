#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, k;
    cin >> n >> k;

    vector<pair<int, int>> meeting(n);
    for (int i=0; i<n; i++) {
        cin >> meeting[i].first >> meeting[i].second;
    }

    sort(meeting.begin(),meeting.end(),[](const auto& a, const auto& b) {
        if (a.second == b.second) return a.first < b.first;
        return a.second < b.second;
    });

    vector<int> rooms(k,0); 
    int answer=0;

    for (const auto& m : meeting) {
        int st=m.first;
        int ed=m.second;

        int idx=-1;
        int maxTime=-1;

        for (int i=0; i<k; i++) {
            if (rooms[i]<st) { // 입장 가능
                if (rooms[i] > maxTime) {
                    maxTime=rooms[i];
                    idx=i;
                }
            }
        }

        if (idx != -1) {
            rooms[idx]=ed;
            answer++;
        }
    }

    cout << answer;
    return 0;
}
