#include <iostream>
#include <vector>
#include <map>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n, m;
    cin >> n >> m;

    string q, a;
    map<string, string> data;
    for (int i=0; i<n; i++) {
        cin >> q >> a;
        data[q]=a;
    }

    string s;
    for (int i=0; i<m; i++) {
        cin >> s;
        vector<string> answer;
        for (int j=0; j<s.size() ; j++) {
            for (int k=0; k<s.size()-j; k++) {
                string target=s.substr(j,k+1);
                if (data[target] != "") {
                    answer.push_back(data[target]);
                }
            }
        }

        if (answer.size()==0) {
            cout << -1 << "\n";
        }else {
            for (auto word : answer) {
                cout << word;
            }
            cout << "\n";
        }

        
    }
    return 0;
}