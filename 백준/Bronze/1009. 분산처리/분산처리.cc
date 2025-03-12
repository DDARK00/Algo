#include <iostream>

int get_last(int a, int b){
    int k = a;
    for (int i=0; i<b-1; i++) {
        k = (k*a)%10;
    }
    k%=10;
    if (k==0)k=10;
    return k;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    int n, a, b, i;
    std::cin >> n;
    for(i=0;i<n;i++){
        std::cin >> a >> b;
        std::cout << get_last(a, b) << "\n";
    }
    return 0;
}