#include <iostream>
#include <map>
#include <set>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    string gen;
    vector<string> gens;
    map<char,int> chk_front;
    map<char,int> chk_back;
    for (int i=0; i<n; i++) {
        cin >> gen;
        chk_front[gen[0]]++;
        chk_back[gen[1]]++;
        gens.push_back(gen);
    }

    set<char> answer;
    for (auto s : gens) {
        chk_front[s[0]]--;
        chk_back[s[1]]--;
        for (char i='A'; i<='Z'; i++) {
            if (chk_front[i]>0) {
                answer.insert(max(i,s[1]));
            }
            if (chk_back[i]>0) {
                answer.insert(max(i,s[0]));
            }
        }
        chk_front[s[0]]++;
        chk_back[s[1]]++;
    }

    cout << answer.size() << "\n";
    for (auto k : answer) {
        cout << k << " ";
    }
    return 0;
}