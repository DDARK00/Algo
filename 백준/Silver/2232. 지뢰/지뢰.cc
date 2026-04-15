#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n, p;
    cin >> n;
    vector<pair<int,int>> arr_origin;
    vector<pair<int,int>> arr_sorted;
    for (int i=0; i<n; i++) {
        cin >> p;
        arr_origin.push_back({p,i});
        arr_sorted.push_back({p,i});
    }

    sort(arr_sorted.begin(),arr_sorted.end(),greater<pair<int,int>>());

    vector<int> answer;
    int target=0;
    while (target<n) {
        auto [dmg, idx]=arr_sorted[target];
        if (arr_origin[idx].first==-1) {
            target++;
            continue;
        }
        answer.push_back(idx+1);
        int nxt_dmg=dmg;
        int nxt_idx=idx-1;
        while (nxt_idx>=0 && arr_origin[nxt_idx].first<nxt_dmg) {
            if (arr_origin[nxt_idx].first==-1) {
                break;
            }
            nxt_dmg=arr_origin[nxt_idx].first;
            arr_origin[nxt_idx].first=-1;
            nxt_idx--;
        }
        
        nxt_dmg=dmg;
        nxt_idx=idx+1;
        while (nxt_idx<n && arr_origin[nxt_idx].first<nxt_dmg) {
            if (arr_origin[nxt_idx].first==-1) {
                break;
            }
            nxt_dmg=arr_origin[nxt_idx].first;
            arr_origin[nxt_idx].first=-1;
            nxt_idx++;
        }

        target++;
    }

    sort(answer.begin(),answer.end());
    for (auto k : answer) {
        cout << k << "\n";
    }
    return 0;
}