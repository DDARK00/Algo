#include <iostream>
using namespace std;

int main() {
    int r,g,b;
    cin >> r >> g >> b;

    int answer=r/3+g/3+b/3;
    r%=3;g%=3;b%=3;
    if (r+g+b == 2){
        answer+=1;
    } else {
        answer+=max(max(r,g),b);
    }
    cout << answer;
    return 0;
}