#include <iostream>
#include <string>
#include <cmath>
 
int main() {
    int n;
    double a, b, temp;
    std::cin >> n;
    a = 0; // 30 10
    b = 0; // 60 15
    for (int i=0; i<n; i++){
        std::cin >> temp;
        a+= ceil((temp+1)/30) *10;
        b+= ceil((temp+1)/60) *15;
    }
    std::string ans = "";
    if (a<=b){
        ans += "Y ";
    }
    if (a>=b){
        ans += "M ";
    }
    std::cout << ans << std::min(a, b);
    return 0;
}