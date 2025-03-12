#include <iostream>
#include <string>
#include <algorithm>

using namespace std;
int main() {
    string a, b;
    cin >> a >> b;
    if (a=="null"){
        cout << "NullPointerException" << "\n" << "NullPointerException";
    }else{
        if(b=="null"){
            cout << "false" << "\n" << "false";
        }else{
            if (a==b){
                cout << "true" << "\n";
            }else{
                cout << "false" << "\n";
            }
            for_each(a.begin(), a.end(), [](auto& k){k=tolower(k);});
            for_each(b.begin(), b.end(), [](auto& k){k=tolower(k);});
            if (a==b){
                cout << "true" << "\n";
            }else{
                cout << "false" << "\n";
            }
        }
    }
    return 0;
}