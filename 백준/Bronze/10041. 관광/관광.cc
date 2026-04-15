#include <iostream>

int main() {
    int x, y, n, nx, ny;
    std::cin >> x >> y >> n;
    int answer=0;
    std::cin >> x >> y;
    for (int i=0; i<n; i++) {
        std::cin >> nx >> ny;
        if ((nx>x&&ny>y)||(nx<x&&ny<y)) {
            answer+=std::max(abs(nx-x),abs(ny-y));
        }else{
            answer+=abs(x-nx);
            answer+=abs(y-ny);
        }
        x=nx;
        y=ny;
    }
    std::cout << answer;
    return 0;
}