#include <iostream>
using namespace std;

int ar[50], n;
bool check(){
    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            if(i==j)continue;
            for (int k=0; k<n; k++) {
                if(i==k)continue;
                if(j==k)continue;
                if((ar[i]-ar[j])%ar[k]!=0){
                    return false;
                }
            }
        }
    }
    return true;
}

int main() {
    cin >> n;
    for (int i=0; i<n; i++) {
        cin >> ar[i];
    }
    if(check()){
        cout << "yes";
    }else{
        cout << "no";
    }
    return 0;
}