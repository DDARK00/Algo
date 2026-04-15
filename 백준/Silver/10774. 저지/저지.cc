#include <iostream>
#include <map>
#include <string>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL); 
    int j, a;
    cin >> j >> a;
    char ot[j+1];
    char size;
    for (int i=0; i<j; i++){
        cin >> size;
        ot[i+1] = size;
    }

    int ans = 0;
    map<char, string> chk={{'S',"SML"}, {'M',"ML"}, {'L',"L"},{'O',""}};
    for (int i=0; i<a; i++){
        cin >> size >> j;
        if (chk[size].find(ot[j]) != string::npos){
            ans++;
            ot[j] = 'O';
        }
    }
    cout << ans;
    return 0;
}