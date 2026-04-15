#include <iostream>
#include <map>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n, p;
    cin >> n >> p;

    int w, l, g;
    cin >> w >> l >> g;

    map<string, bool> data;
    string name, type;
    for (int i=0; i<p; i++) {
        cin >> name >> type;
        data[name]=type=="W"?1:0;
    }

    int score=0;
    bool rank=false;
    for (int i=0; i<n; i++) {
        cin >> name;
        if (data[name]) {
            score+=w;
        } else {
            score=max(0,score-l);
        }
        if (score>=g) {
            rank=true;
        }
    }

    if (rank) {
        cout << "I AM NOT IRONMAN!!";
    } else {
        cout << "I AM IRONMAN!!";
    }
    return 0;
}
