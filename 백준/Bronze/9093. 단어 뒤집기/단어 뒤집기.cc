#include <iostream>
#include <sstream>
using namespace std;

void solve(){
    string s, temp;
    getline(cin, s, '\n');
    stringstream ss(s);
    while(ss >> temp){
        for (int i=temp.size()-1; i>=0; i--) {
            cout << temp[i];
        }
        cout << " ";
    }
    cout << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    cin >> n;

    cin.ignore();
    for (int i=0; i<n; i++) {
        solve();
    }
    return 0;
}