#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n;
    while(true){
        cin >> n;
        if(n==0)break;
        int station[n];
        for(int i=0;i<n;i++){
            cin >> station[i];
        }
        sort(station,station+n);

        int go = 0;
        bool ok = true;
        for (auto num:station){ 
            if(go>=num){
                go = num+200;
                if(go>=1422)break;
            }else{
                ok = false;
                break;
            }
        }
        if ((1422 - station[n-1])>100){
            ok = false;
        }
        if(ok && go>=1422){
            cout << "POSSIBLE" << "\n";
        }else{
            cout << "IMPOSSIBLE" << "\n";
        }
    }
    return 0;
}