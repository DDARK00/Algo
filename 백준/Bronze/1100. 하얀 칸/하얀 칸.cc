#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int answer=0;
    string temp;
    for (int i=0; i<8; i++){
        cin >> temp;
        for (int j=0; j<8; j++) {
            if ((i+j)%2)continue;
            if (temp[j]=='F')answer+=1;
        }
    }
    cout << answer;
    return 0;
}