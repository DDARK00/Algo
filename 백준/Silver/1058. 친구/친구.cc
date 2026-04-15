#include <iostream>
#include <set>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    string temp;
    cin >> n;
    vector<string> graph(n);
    for (int i=0; i<n; i++) {
        cin >> graph[i];
    }

    // 50*50*50 2500*50 125000
    int answer=0;
    for (int i=0; i<n; i++) {
        set<int> two_fr;
        int test=0;
        for (int j=0; j<n; j++) {
            if (graph[i][j]=='Y') {
                two_fr.insert(j);
                for (int k=0; k<n; k++) {
                    if (graph[j][k]=='Y') {
                        two_fr.insert(k);
                        test++;
                    }
                }
            }
        }
        answer=max(answer,(int)two_fr.size());
        // cout << test << "\n";
    }

    cout<<max(0,answer-1);
    return 0;
}