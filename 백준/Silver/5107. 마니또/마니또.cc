#include <iostream>
#include <map>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, tc=1;
    cin >> n;
    while (n!=0) {
        string a, b;
        map<string,string> data;
        map<string,bool> visited;
        vector<string> saram;
        for (int i=0; i<n; i++) {
            cin >> a >> b;
            data[a]=b;
            saram.push_back(a);
        }

        int answer=0;
        string daum_saram="";
        for (auto s : saram) {
            if (!visited[s]) {
                answer++;
                daum_saram=data[s];
                visited[s]=1;
                while (!visited[daum_saram]) {
                    visited[daum_saram]=1;
                    daum_saram=data[daum_saram];
                }
            }
        }

        cout << tc << " " << answer << "\n";
        cin >> n;
        tc++;
    }
    return 0;
}