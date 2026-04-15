#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, d;
    cin >> n >> d;

    auto cmp=[](auto a, auto b){return a.first<b.first;};
    priority_queue<pair<long long,int>, vector<pair<long long, int>>, decltype(cmp)> pq(cmp);

    long long tmp;
    long long answer=-100000001;
    pq.push({-1000000001,-100001}); // 1e9 1e5
    for (int i=0; i<n; i++) {
        cin >> tmp;

        while (!pq.empty() && pq.top().first<0){
            pq.pop();
        }
        while (!pq.empty()&&(i-pq.top().second)>d){
            pq.pop();
        }
        if (!pq.empty()&&(pq.top().first+tmp)>0){
            pq.push({pq.top().first+tmp,i});
        }
        pq.push({tmp,i});
        answer=max(answer,pq.top().first);
    }

    cout << answer;
    return 0;
}