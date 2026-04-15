#include <iostream>
using namespace std;

void solve(){
    int n, mx=0, all=0;
    int temp, ans;
    bool b = false;
    cin >> n;
    for (int i=0; i<n; i++){
        cin >> temp;
        if (temp>mx){
            mx=temp;
            ans=i;
            b=false;
        }else if(temp==mx){
            b=true;
        }
        all+=temp;
    }

    if(b){
        cout << "no winner" << "\n";
    }else{
        if(all/2 < mx){
            cout << "majority winner " << ans+1 <<"\n";
        }else{
            cout << "minority winner " << ans+1 <<"\n";
        }
    }
}


int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin >> t;
    for (int i=0; i<t; i++){
        solve();
    }
    return 0;
}