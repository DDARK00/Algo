#include <iostream>
#include <string>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n, d, k, c;
    cin >> n >> d >> k >> c;
    int chk[30001]{};
    int dish[30001];

    int answer=0, temp=0;
    for (int i=0; i<n; i++) {
        cin >> dish[i];
    }

    for (int i=0; i<k; i++) {
        if (chk[dish[i]]==0) {
            temp++;
        }
        chk[dish[i]]++;
    }
    answer=temp;
    for (int i=k; i<n*2+2; i++) {
        if (chk[dish[i%n]]==0) {
            temp++;
        }
        chk[dish[i%n]]++;
        if (chk[dish[(i-k)%n]]==1){
            temp--;
        }
        chk[dish[(i-k)%n]]--;
        answer=max(answer,temp+(chk[c]>0?0:1));
    }

    cout << answer;
    return 0;
}