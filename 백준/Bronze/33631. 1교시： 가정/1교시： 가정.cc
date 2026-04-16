#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int f, c, e, b;
    cin >>f>>c>>e>>b;
    int wf, wc, we, wb;
    cin >>wf>>wc>>we>>wb;

    int q, qi, qt;
    cin >> q;
    int maked = 0;
    for (int i=0;i<q; i++) {
        cin>>qi>>qt;
        if (qi==1){
            if(qt*wf<=f &&qt*wc<=c &&qt*we<=e &&qt*wb<=b){
                f-= qt*wf;
                c-= qt*wc;
                e-= qt*we;
                b-= qt*wb;
                maked +=qt;
                cout << maked << "\n";
            }else{
                cout << "Hello, siumii" << "\n";
            }
        }else if(qi==2){
            f+= qt;
            cout << f << "\n";
        }else if(qi==3){
            c+= qt;
            cout << c << "\n";
        }else if(qi==4){
            e+= qt;
            cout << e << "\n";
        }else if(qi==5){
            b+= qt;
            cout << b << "\n";
        }
    }
    return 0;
}