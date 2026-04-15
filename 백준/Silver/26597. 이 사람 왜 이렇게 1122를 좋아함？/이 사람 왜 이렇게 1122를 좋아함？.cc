#include <iostream>
#include <vector>
using namespace std;


void solve(int n){
    long long k;
    char ud;

    long long bot=-1LL*1000000000000000000-1;
    long long top=1LL*1000000000000000000+1;
    int digit;
    bool find=false;
    for (int i=0; i<n; i++) {
        cin >> k >> ud;
        if (ud=='^'){
            bot=max(bot,k);
        }else{
            top=min(top,k);
        }

        if (bot+1>=top) {
            cout << "Paradox!" << "\n" << i+1;
            return;
        }else if (top-bot == 2 && !find) {
            digit = i+1;
            find=true;
        }
    }

    if (find) {
        cout << "I got it!" <<"\n" << digit;
    }else{
        cout << "Hmm...";
    }
    return;
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    cin >> n;

    solve(n);
    return 0;
}