#include <iostream>
#include <vector>
using namespace std;
bool solve(string w, vector<int> alpha);
int main() {
    int t;
    cin >> t;
    for (int tc=0; tc<t; tc++){
        vector<int> alpha(26, 0);
        string s;
        cin >> s;
        for (int i=0; i<s.size(); i++) {
            alpha[s[i]-'A']++;
        }
        int w;
        string q;
        cin >> w;
        for (int i=0; i<w; i++){
            cin >> q;
            if (solve(q, alpha)){
                cout << "YES" <<"\n";
            }else{
                cout << "NO" <<"\n";
            }
        }
    }
    return 0;
}
bool solve(string query, vector<int> alpha){
    bool ok = true;
    for (int i=0; i<query.size(); i++){
        int target = query[i]-'A';
        if (alpha[target]==0){
            ok=false;
            break;
        }
        alpha[target]-=1;
    }
    return ok;
}