#include <iostream>
 
using namespace std;
int main() {
    long n, r, c;
    cin >> n >> r >> c;
    long long ans;
    if (n==3){
        if (r==2 && c==2){
            ans = 1;
        }else{
            ans = 4;
        }
    }else{
        ans = (n*n)/2;
        if(n%2 && (r+c)%2==0){
            ans+=1;
        }
    }
    cout << ans;
    return 0;
}