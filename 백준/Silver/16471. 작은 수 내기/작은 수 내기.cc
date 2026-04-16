#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, tmp;
    cin >> n;

    vector<int> my;
    vector<int> yours;
    for (int i=0; i<n; i++) {
        cin >> tmp;
        my.push_back(tmp);
    }
    sort(my.begin(),my.end());
    for (int i=0; i<n; i++) {
        cin >> tmp;
        yours.push_back(tmp);
    }
    sort(yours.begin(),yours.end());
    int answer=0, i=0, j=0;
    while (i<n && j<n) {
        if (my[i]<yours[j]) {
            answer++;
            i++;
            j++;
        } else{
            j++;
        }
    }

    if (answer>n/2) {
        cout << "YES";
    } else {
        cout << "NO";
    }
    return 0;
}