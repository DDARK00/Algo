#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    string p_name;
    int need_candy, had_candy;

    string answer="";
    int answer_cnt=0, answer_sum_cnt=0;
    for (int i=0; i<n; i++) {
        cin >> p_name;
        cin >> need_candy >> had_candy;
        int now_cnt=0;
        while (had_candy>=need_candy) {
            now_cnt++;
            had_candy-=need_candy;
            had_candy+=2;
            answer_sum_cnt++; // 수학? 몰?루
        }

        if (answer_cnt<now_cnt) {
            answer=p_name;
            answer_cnt=now_cnt;
        }
    }

    cout << answer_sum_cnt << "\n" << answer;
    return 0;
}