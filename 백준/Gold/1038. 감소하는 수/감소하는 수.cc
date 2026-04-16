#include <iostream>
#include <vector>
using namespace std;

vector<string> answer;
int idx=-1, l=0;
vector<int> selected;

void dfs(int depth){
    if (selected.size()-1==l) {
        string temp="";
        for (int i=1; i<selected.size(); i++) {
            temp+=selected[i]+'0';
        }
        idx++;
        answer.push_back(temp);
        return;
    }

    for (int i=0; i<10; i++) {
        if (selected[depth]>i) {
            selected.push_back(i);
            dfs(depth+1);
            selected.pop_back();
        }
    }
}

// 9876543210
void solve(){
    selected.push_back(10);
    for (int i=0; i<10; i++) {
        l++;
        dfs(0); // i자리
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    cin >> n;
    solve();
    if (n>idx) {
        cout << -1;
    }else{
        cout << answer[n];
    }
    return 0;
}