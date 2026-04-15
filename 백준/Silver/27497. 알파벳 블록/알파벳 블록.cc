#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    cin >> n;

    deque<string> answer;
    int k;
    vector<int> cmd;
    string s;
    for (int i=0; i<n; i++) {
        cin >> k;
        if (k==1) {
            cin >> s;
            answer.push_back(s);
            cmd.push_back(1);
        } else if (k==2) {
            cin >> s;
            answer.push_front(s);
            cmd.push_back(2);
        } else {
            if (cmd.size()>0 && answer.size()>0) {
                if (cmd.back()==1) {
                    answer.pop_back();
                    cmd.pop_back();
                } else {
                    answer.pop_front();
                    cmd.pop_back();
                }
            }
        }
    }

    for (auto c : answer) {
        cout << c;
    }
    if (answer.size()==0) {
        cout << 0;
    }
    return 0;
}