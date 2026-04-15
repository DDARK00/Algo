#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout << fixed;
    cout.precision(12);

    int n, k;
    double s;
    cin >> n >> s >> k;

    int madi=1, beat;
    double answer=0;
    for (int i=0; i<k; i++) {
        // 60bpm 4beat 1s
        cin >> beat;
        answer+=(beat-madi)*4/(s/60);
        madi=beat;
        cin >> s;
    }
    answer+=(n+1-madi)*4/(s/60);

    
    cout << answer << "\n";
    return 0;
}