#include <iostream>
#include <map>
#include <bitset>
using namespace std;

bitset<5001> book_genre[200]; // 역색인 장르->책
bitset<5001> result; // 필터 결과

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    cin >> n;

    string s;
    map<string,int> genre;
    for (int i=0; i<n; i++) {
        cin >> s;
        genre[s]=genre.size();
    }

    int m, k;
    cin >> m;
    for (int i=0; i<m; i++) {
        cin >> k >> s;
        for (int j=0; j<k; j++) {
            cin >> s;
            book_genre[genre[s]].set(i);
        }
    }

    int q;
    cin >> q;
    for (int i=0; i<q; i++) {
        result.set();
        cin >> k;
        for (int j=0; j<k; j++) {
            cin >> s;
            result &=book_genre[genre[s]];
        }
        cout << result.count() << "\n";
    }
    return 0;
}