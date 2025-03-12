#include <iostream>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int a, b;
    cin >> a >> b;
    string ans;
    if(a>b){
        ans = ">";
    }else if (a<b){
        ans = "<";
    }else{
        ans = "==";
    }
    cout << ans << "\n";
    return 0;
}