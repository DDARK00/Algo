#include <iostream>
#include <unordered_map>
using namespace std;
 
int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    long long b,n,m;
    cin>>b>>n>>m;
    string name;
    long long price;
    unordered_map<string, long long> data;
    for (int i=0; i<n; i++) {
        cin>>name>>price;
        data.insert({name,price});
    }
    long long needs = 0;
    for (int i=0; i<m; i++) {
        cin>>name;
        needs += data[name];
    }
    if (needs<=b){
        cout << "acceptable";
    }else{
        cout << "unacceptable";
    }
    return 0;
}