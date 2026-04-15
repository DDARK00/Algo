#include <iostream>

int main() {
    int n;
    std::cin >> n;
    // 1 2  2  1  3 16 1  4 256 1  5 65535 1 6 ???
    if(n==1){
        std::cout << 2;
    }else{
        std::cout << 1;
    }
    return 0;
}