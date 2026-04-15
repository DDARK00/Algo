#include <iostream>
using namespace std;

int main() {
    int a, b, c;
    cin >> a >> b >> c;
    a+=b;
    if (a-c-c>=0){
        cout << a-c-c;
    }else{
        cout << a;
    }
    return 0;
}