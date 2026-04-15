#include <iostream>
using namespace std;

int main() {
    int a,b,c,d,e,f;
    cin>>a>>b>>c>>d>>e>>f;
    int k=min(a,d), l=min(b,c);
    k=min(k,e); l=min(l,f);
    k=min(k,l+1);
    l=min(l,k+1);
    cout << k+l;
    return 0;
}