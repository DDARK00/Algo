#include <iostream>
#include <vector>
using namespace std;

int main() {
    int k, a1, a2, a3, b1, b2, b3;
    cin >> k;
    vector<vector<int>> grid(10, vector<int>(10,1));

    for (int i=0; i<k; i++) {
        cin >> a1 >> a2 >> a3 >> b1 >> b2 >> b3;
        for (int i=0; i<10; i++) {
            for (int j=0; j<10; j++) {
                if (i==a1-1|| i==a2-1 || i==a3-1 || j==b1-1 || j==b2-1 || j==b3-1){
                    grid[i][j]=1;
                }else{
                    grid[i][j]++;
                }
            }
        }
    }

    for (auto g : grid) {
        for (auto el : g) {
            cout << el << " ";
        }
        cout << "\n";
    }
    return 0;
}