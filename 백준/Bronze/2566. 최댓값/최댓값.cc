#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int max_val=-1;
    int a, b;

    for(int i=0;i<81;i++){
        int val;
        cin>>val;

        if (max_val<val){
            max_val = val;
            a = i/9 +1;
            b = i%9 +1;
        }
    }

    cout<<max_val<<"\n";
    cout<<a<<" "<< b;
    return 0;
}