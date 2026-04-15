#include <iostream>

int main() {
    long long n, answer=1, k=1;
    std::cin >> n;
    long long p=n;
    if (n==0) {
        std::cout << 0;
        return 0;
    }

    while ((double)n/2>k){
        k<<=1;
        answer++;
    }

    if (n==k) {
        std::cout <<  answer;
    }else{
        std::cout <<  answer+1;
    }
    return 0;
}