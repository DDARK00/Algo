#include <iostream>
#include <string>
#include <tuple>
using namespace std;


int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    string temp;
    cin >> temp;

    string hh = "";
    string mm = "";
    hh.append(1, temp[0]);
    hh.append(1, temp[1]);
    mm.append(1, temp[3]);
    mm.append(1, temp[4]);

    int time = 0;
    time += stoi(hh) * 60;
    time += stoi(mm);
    time %= 720;
    
    int hp[6];
    for(int i=0; i<6; i++){
        cin >> hp[i];
    }
    
    int l;
    cin >> l;

    // for 2 hour / 1block
    for(int i=0; i<l; i++){
        double pos;
        string cmd;
        cin >> pos >> cmd;
        if (pos>60){
            break;
        }
        if (cmd == "^"){
            hp[time/120] = 0;
        }else{
            int added = cmd[0] - '0';
            if(cmd[2]=='M'){
                time += added*10;
            }else{
                time += added*60;
            }
            time %= 720;
        }
    }

    int ans = 0;
    for(int num: hp){
        ans += num;
    }
    cout << min(ans, 100) << "\n";
    return 0;
}