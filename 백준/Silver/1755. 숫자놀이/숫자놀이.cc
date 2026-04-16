#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int n, m;
    cin >> n >> m;
    string arr[10]={
    "zero","one","two","three","four","five","six","seven","eight","nine"
    };

    auto cmp = [](auto a, auto b){return a.first>b.first;};
    priority_queue<pair<string,int>,vector<pair<string,int>>,decltype(cmp)> pq(cmp);

    string temp;
    for (int i=n; i<m+1; i++) {
        temp=i<10?"":arr[i/10];
        temp+=arr[i%10];
        pq.push({temp,i});
    }

    for (int i=1; i<m-n+2; i++) {
        cout << pq.top().second << " ";
        pq.pop();
        if (i%10==0) {
            cout << "\n";
        }
    }
    return 0;
}