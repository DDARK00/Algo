#include <iostream>

int main() {
    int n, m;
    std::cin >> n >> m;

    int answer=0, dock[n+1];
    dock[0]=0;
    for (int i=1; i<n+1; i++) {
        std::cin >> dock[i];
    }

    int l=0, r=0, target=dock[0];
    while (1) {
        // std::cout << l << " l : r " << r << " " << target <<"\n";

        if (target<=m) {
            r++;
            if (r==n+1) break;
            target+=dock[r];
        }else{
            target-=dock[l];
            l++;
        }

        if (target<=m) {
            answer=std::max(answer,target);
        }

    }

    std::cout << answer;
    return 0;
}