#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int y, temp;
    cin >> y;

    temp = 0;
    for (int i=y+1; i<9999; i++){
        temp += i/100;
        temp += i%100;
        if (temp * temp == i){
            temp = i;
            break;
        }else {
            temp = 0;
        }
    }
    if (temp != 0){
        cout << temp;
    }else {
        cout <<-1;
    }
    return 0;
}