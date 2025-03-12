#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n, m, k;
    cin >> n >> m;
    unordered_map<string, vector<string>> members;
    unordered_map<string, string> teams;

    string temp, temp2;
    for (int i=0; i<n; i++){
        cin >> temp;
        cin >> k;
        members[temp] = {};
        for (int j=0; j<k; j++){
            cin >> temp2;
            teams[temp2] = temp;
            members[temp].push_back(temp2);
        }
    }

    for (int i=0; i<m; i++) {
        cin >> temp >> k;
        if (k){
            cout << teams[temp] << "\n";
        }else{
            sort(members[temp].begin(), members[temp].end());
            for (auto name : members[temp]) {
                cout << name << "\n";
            }
        }
    }
    return 0;
}