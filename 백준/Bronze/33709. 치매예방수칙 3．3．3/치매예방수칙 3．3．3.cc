#include <iostream>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    string temp = "", s;
    long long ans = 0;

    int n;
    cin >> n >> s;
    int size = s.size();

    for (int i=0; i<size; i++){
        if (s[i]=='.'|| s[i] =='|'||s[i]==':'||s[i]=='#'){
            ans += stoi(temp);
            temp = "";
        }else{
            temp+=s[i];
        }
    }
    ans += stoi(temp);
    cout << ans;
    return 0;
}