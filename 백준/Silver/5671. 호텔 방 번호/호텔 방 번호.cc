#include <iostream>
#include <set>
#include <string>
using namespace std;

int main() {
    int n, m, ans;
    string temp;

    while(cin >> n >> m){
        ans = 0;
        for(int i=n; i<m+1; i++){
            set<char> chk;
            temp = to_string(i);
            for(char k:temp){
                chk.insert(k);
            }
            if (temp.size()==chk.size()) ans+=1;
        }
        cout << ans << "\n";
    }
    return 0;
}