#include <iostream>
#include <map>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    bool signs[1000];
    signs[0]=1;
    // 0 or 1 -> p or m
    // pp p mm p pm m mp m dif is m

    int n;
    char c;
    cin >> n;
    for (int i=1; i<n; i++) {
        cout << "? " << i << " * " << i+1 << "\n" << flush;
        cin >> c;
        signs[i]=c=='+'?signs[i-1]:signs[i-1]^1;
    }

    // +--
    int s=0, find=-1;
    for (int i=1; i<n; i++) {
        if (signs[0]==signs[i]) {
            find=i;
            break;
        }
    }

    if (find==-1) {
        s=1;
        find=2;
    }
    cout << "? " << s+1 << " + " << find+1 << "\n" << flush;

    char answer[2]={'-','+'};
    char result[2];
    cin >> c;
    if (c=='+') {
        result[signs[find]]='+';
        result[signs[find]^1]='-';
    } else {
        result[signs[find]]='-';
        result[signs[find]^1]='+';
    }

    cout << "!";
    for (int i=0; i<n; i++) {
        cout << " " << result[signs[i]];
    }
    cout << "\n" << flush;
    return 0;
}