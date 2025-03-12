#include <iostream>
#include <string>
using namespace std;
 
bool check(string s, int size){
    bool chk = true;
    for (int i=0; i<size/2; i++) {
        if(s[i]!=s[size-1-i]){
            chk = false;
            break;
        }
    }
    return chk;
}
 
int calc(string a){
    int temp;
    int ans=0;
    int size = a.size();
    while (true){
        if(check(a, size))break;
        ans+=1;
        temp = stoi(a) +1;
        a = to_string(temp);
        a = string((size-a.size()),'0')+a;
    }
    return ans;
}
 
int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    string s;
    while(true){
        cin >> s;
        if (s=="0")break;
        cout << calc(s) << "\n";
    }
    return 0;
}