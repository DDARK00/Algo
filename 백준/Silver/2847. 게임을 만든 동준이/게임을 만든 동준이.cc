#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    cin >> n;
    int score[100];
    for (int i=0; i<n; i++) {
        cin >> score[i];
    }
    int answer=0, diff;
    for (int i=n-2; i>=0; i--) {
        if (score[i+1]>score[i]) continue;
        diff=score[i]-(score[i+1]-1);
        answer+=diff;
        score[i]-=diff;
    }
    cout << answer;
    return 0;
}