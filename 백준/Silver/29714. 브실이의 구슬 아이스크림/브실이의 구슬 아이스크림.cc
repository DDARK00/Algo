#include <iostream>
#include <map>
#include <vector>
using namespace std;

int n;
vector<int> answer;
map<int,int> colors;

void run_query(){
    int a, b, tmp;
    cin >> a;
    map<int, int> target;
    for (int i=0; i<a; i++) {
        cin >> tmp;
        target[tmp]++;
    }

    bool run_flag=true;
    for (auto k : target) {
        if (colors[k.first] < k.second) {
            run_flag=false;
        }
    }

    cin >> b;
    if (run_flag){
        for (auto k : target) {
            colors[k.first]-=k.second;
        }
    }

    for (int i=0; i<b; i++) {
        cin >> tmp;
        if (run_flag) {
            colors[tmp]++;
        }
    }
}

void process(){
    for (auto k : colors) {
        for (int i=0; i<k.second; i++) {
            answer.push_back(k.first);
        }
    }
}

void print(){
    cout << answer.size() << "\n";
    for (auto k : answer) {
        cout << k << " ";
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    // init
    int temp;
    cin >> n;
    for (int i=0; i<n; i++) {
        cin >> temp;
        colors[temp]++;
    }

    int q;
    cin >> q;
    for (int i=0; i<q; i++) {
        run_query();
    }

    process();

    print();
    return 0;
}