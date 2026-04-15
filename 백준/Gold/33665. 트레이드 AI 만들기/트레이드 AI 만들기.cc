#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> values(10, vector<int>(5,0)); // 점령 가치
int citys[10][2]{}; // 소유중 카운트 0나 1상대
int city_idx[10][4]{}; // 소유중 인덱스 1나 2상대

vector<pair<int,int>> my_item; // 교환 매물 내꺼
vector<pair<int,int>> your_item; // 교환 매물 상대꺼

int pawn_city[10][4]; // 담보 상태
int w, p; // 현금가중치, 담보패널티

// 도시
void calc_citys_value(vector<int>&assets){
    for (int i=0; i<10; i++) {
        assets[0]+=values[i][citys[i][0]];
        assets[1]+=values[i][citys[i][1]];
    }
}

//현금
void calc_money_value(vector<int>&assets, int my_money, int your_money){
    assets[0]+=my_money*w/100;
    assets[1]+=your_money*w/100;
}

// 담보 패널티
void calc_penalty_value(vector<int>&assets){
    for (int i=0; i<10; i++) {
        for (int j=0; j<4; j++) {
            if (pawn_city[i][j]){
            assets[city_idx[i][j]-1]-=p;
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    // init
    // 도시 점령 가치
    for (int i=0; i<10; i++) {
        cin >> values[i][1] >> values[i][2] >> values[i][3] >> values[i][4];
    }

    // 도시 소유 상태
    string s;
    cin >> s;
    for (int i=0; i<10; i++) {
        for (int j=0; j<4; j++) {
            if (s[i*4+j]=='1') {
                citys[i][0]++;
                city_idx[i][j]=1;
            }else if (s[i*4+j]=='2'){
                citys[i][1]++;
                city_idx[i][j]=2;
            }
        }
    }

    cin >> s;
    // trade target 교환 대상
    for (int i=0; i<10; i++) {
        for (int j=0; j<4; j++) {
            if (s[i*4+j]=='1') {
                my_item.push_back({i,j}); // i색의 j번째 도시
            }else if (s[i*4+j]=='2'){
                your_item.push_back({i,j});
            }
        }
    }

    cin >> s;
    // 도시 담보 현황
    for (int i=0; i<10; i++) {
        for (int j=0; j<4; j++) {
            pawn_city[i][j]=s[i*4+j]-'0';
        }
    }
    
    // 현재 내 돈 니 돈
    int my_money, your_money;
    cin >> my_money >> your_money;

    // 주고받는 돈
    int sent_money, get_money;
    cin >> sent_money >> get_money;

    // 현금가중치, 담보패널티
    cin >> w >> p;

    // 재산 현황
    vector<int> assets = {0, 0};

    // 트레이드 전의 재산 가치
    // 도시
    calc_citys_value(assets);

    // 현금
    calc_money_value(assets, my_money, your_money);

    // 담보 패널티
    calc_penalty_value(assets);

    int before_diff=assets[0]-assets[1]; // 거래 전
    // cout << assets[0] << " " << assets[1] << " " << before_diff << "\n";

    // 거래 과정
    // 현금거래
    my_money=my_money-sent_money+get_money;
    your_money=your_money-get_money+sent_money;

    // 도시거래 내가 원하는거 <-> 상대가 원하는거
    for (auto k : my_item) {
        auto [i,j]=k;
        citys[i][1]--;
        citys[i][0]++;
        city_idx[i][j]=1;
    }
    for (auto k : your_item) {
        auto [i,j]=k;
        citys[i][0]--;
        citys[i][1]++;
        city_idx[i][j]=2;
    }

    // 트레이드 이후 재산 가치
    assets = {0, 0};
    
    // 도시
    calc_citys_value(assets);

    // 현금
    calc_money_value(assets, my_money, your_money);

    // 담보 패널티
    calc_penalty_value(assets);
    
    int after_diff=assets[0]-assets[1]; // 거래 전
    // 인터페이스 분리할걸 그랬나?
    // cout << assets[0] << " " << assets[1] << " " << after_diff << "\n";

    if (before_diff<=after_diff) {
        cout << "YES";
    }else{
        cout << "NO";
    }
    return 0;
}