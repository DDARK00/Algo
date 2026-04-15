#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    cin >> n;

    // monotone
    int a, b;
    vector data={0};
    for (int i=0; i<n; i++) {
        cin >> a >> b;
        if (a==2) {
            int target=max(0,data[data.size()-1]-b);
            data.pop_back();
            data.push_back(target);
        } else {
            data.push_back(b);
        }
    }

    int i=data.size()-1;
    long long answer=data[i];
    int limit=data[i];
    for (int j=i-1; j>0; j--) {
        limit=min(limit,data[j]);
        answer+=limit;
    }

    cout << answer;
    return 0;
}