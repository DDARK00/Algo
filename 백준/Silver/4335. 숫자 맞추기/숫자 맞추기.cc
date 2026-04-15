#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    string s;
    int bt=0, top=11;

    bool answer=true;
    while (true) {
        cin >> n;
        if (n==0) break;
        cin >> s >> s;
        if (s=="high") {
            if (n<=bt) {
                answer=false;
            }
            top=min(top,n);
        } else if (s=="low") {
            if (n>=top) {
                answer=false;
            }
            bt=max(bt,n);
        } else {
            if (answer&&(bt>=n||top<=n)) {
                answer=false;
            }
            if (answer) {
                cout << "Stan may be honest\n";
            } else {
                cout << "Stan is dishonest\n";
            }
            bt=0, top=11;
            answer=true;
        }
    }
    return 0;
}