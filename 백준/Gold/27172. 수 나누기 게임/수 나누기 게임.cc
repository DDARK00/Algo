#include <iostream>
#include <vector>
using namespace std;

const int MAX_VALUE = 1000001;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n;
    cin >> n;

    int cards[MAX_VALUE] ={0};

    int user[n+1];
    for (int i=0;i<n;i++){
        cin>>user[i];
        cards[user[i]]=i+1;
    }

    vector<int> ans(n, 0);
    for (int i = 1; i<MAX_VALUE; i++) {
        if (cards[i]){
            for(int j = i;j<MAX_VALUE;j+=i){
                if(cards[j]){
                    ans[cards[i]-1]+=1;
                    ans[cards[j]-1]-=1;
                }
            }
        }
    }
    
    for(int k:ans){
        cout << k << " ";
    }
    
    return 0;
}