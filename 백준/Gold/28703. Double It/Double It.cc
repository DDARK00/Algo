#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n, mx=0, tmp;
    cin >> n;

    priority_queue<int,vector<int>,greater<int>> pq;
    for (int i=0; i<n; i++) {
        cin >> tmp;
        mx=max(mx,tmp);
        pq.push(tmp);
    }

    int origin_mx=mx, answer=1000000007;
    // 기존의 최대와 가장 가까운 수?
    while (pq.top()<=origin_mx){
        tmp=pq.top();
        pq.pop();
        answer=min(answer,mx-tmp);
        pq.push(tmp*2);
        mx=max(mx,tmp*2);
    }

    cout << answer;
    return 0;
}