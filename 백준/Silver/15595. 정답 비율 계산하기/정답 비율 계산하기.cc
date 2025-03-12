#include <iostream>
#include <unordered_map>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    cin >> n;
    double wa_cnt = 0;
    unordered_map<string, int> g;
    unordered_map<string, bool> chk;
    // wa, solve
    for(int i=0; i<n; i++){
        string no, uid, rst, mem, tim, lang, len;
        cin >> no>>uid>>rst>>mem>>tim>>lang>>len;
        if(uid == "megalusion")continue;
        if(rst =="4"){
            chk[uid]=true;
            wa_cnt += g[uid];
            g[uid]=0;
        }else if(!chk[uid]){
            g[uid]+=1;
        }
    }
    double solve_cnt = 0;
    for(auto const&[key, value]:chk){
        solve_cnt+= value;
    }
    if (solve_cnt == 0) {
        cout << 0;
    }else{
        double ans;
        ans = solve_cnt / (solve_cnt+wa_cnt) * 100;
        cout << fixed;
        cout.precision(15);
        cout <<ans <<"\n";
    }
    return 0;
}