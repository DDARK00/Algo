#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n, an, bn;
    cin >> n >> an >> bn;

    int round = 1;
    while (true){
        if((an%2 && an+1 == bn)||(bn%2 && bn+1 ==an))break;
        an = (an+1)/2;
        bn = (bn+1)/2;
        round ++;
    }
    cout << round;
    return 0;
}