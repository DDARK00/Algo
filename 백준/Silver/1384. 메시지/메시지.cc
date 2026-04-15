#include <iostream>
#include <vector>
using namespace std;

int main() {
    cin.tie(0);
    ios::sync_with_stdio(0);

    int no=1, t;
    string tmp;
    cin >> t;
    while (t!=0){
        vector<vector<string>> names(t);
        for (int i=0; i<t; i++) {
            for (int j=0; j<t; j++) {
                cin >> tmp;
                names[i].push_back(tmp);
            }
        }

        cout << "Group " << no << "\n";
        vector<string> answer;
        for (int i=0; i<t; i++) {
            for (int j=1; j<t; j++) {
                if (names[i][j]=="N"){
                    answer.push_back(names[(i-j+t)%t][0] + " was nasty about " + names[i][0] + "\n");
                }
            }
        }

        if (answer.size()>0) {
            for (auto k : answer) {
                cout << k;
            }
        }else{
            cout << "Nobody was nasty" << "\n";
        }
        cin >> t;
        no++;
        cout << "\n";
        
    }
    return 0;
}