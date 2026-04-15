#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    string s;
    getline(cin, s);
    // cout << 'A'-'a' << ' ';
    for (int i=0; i<s.size(); i++) {
        if (s[i]-'A'<0){
            cout << s[i];
        }else if(s[i]<'a'){
            cout << char('A'+(s[i]-'A'+13)%26);
        }else{
            cout << char('a'+(s[i]-'a'+13)%26);
        }
    }
    return 0;
}