#include <iostream>
#include <string>
using namespace std;


string sol(int n){
    pair<string, int> chk[n+1]{};

    string temp;
    getline(cin, temp);
    for (int i=0; i<n; i++) {
        getline(cin, temp);
        chk[i+1] = {temp, 0};
    }
    int num;
    for (int i=0; i<n*2-1; i++){
        cin >> num >> temp;
        chk[num].second +=1;
    }
    string ans = "";
    for (auto k :chk){
        if(k.second == 1){
            ans = k.first;
            break;
        }
    }
    return ans;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n, t=1;

    while (true){
        cin >> n;
        if(n==0)break;
        cout << t << " " << sol(n) << "\n";
        t++;
    }

    return 0;
}