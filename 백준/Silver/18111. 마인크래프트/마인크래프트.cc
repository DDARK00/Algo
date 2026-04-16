#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n, m, b;
    cin >> n >> m >> b;
    int wh = n*m;
    int ttang[wh];
    int mx=0, mn=1000001;
    for (int i=0; i<wh; i++) {
        cin >> ttang[i];
        mx=max(mx,ttang[i]);
        mn=min(mn,ttang[i]);
    }

    // 256~0
    int answer=1e9, temp;
    for (int i=mx; i>=mn; i--) {
        // delete 2s  add 1s
        int overs=0;
        int needs=0;

        for (int j=0; j<wh; j++) {
            if (ttang[j]>i) {
                overs += ttang[j]-i; // delete
            }else{
                needs += i-ttang[j]; // add
            }
        }
        // cout << "높이 : " << i << "\n";
        // cout <<"needs: "<< needs << " / overs : " << overs <<"\n";
        if ((overs+b)<needs)continue;
        if (answer > needs+overs*2){
            answer = needs+overs*2;
            temp=i;
        }
    }
    cout<<answer <<" "<<temp;
    return 0;
}