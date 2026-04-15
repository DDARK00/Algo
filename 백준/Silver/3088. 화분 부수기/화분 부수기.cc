#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n, a, b, c;
    bool hit[1000001]{};
    cin >> n;
    int answer=0;
    for (int i=0; i<n; i++) {
        cin >> a >> b >> c;
        if (!hit[a]&&!hit[b]&&!hit[c]){
            answer++;
        }
        hit[a]=1;
        hit[b]=1;
        hit[c]=1;
    }
    cout << answer;
    return 0;
}