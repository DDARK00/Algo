#include <iostream>
#include <algorithm>
#include <bitset>
#include <string>
using namespace std;
string opcode[24]={"ADD","ADDC","SUB","SUBC","MOV","MOVC","AND","ANDC","OR","ORC","NOT","","MULT","MULTC","LSFTL","LSFTLC","LSFTR","LSFTRC","ASFTR","ASFTRC","RL","RLC","RR","RRC"};

void solve(){
    string cmd;
    int d, a, c_or_b;
    cin >> cmd;
    cin >> d >> a >> c_or_b;
    bitset<5> dec_to_bin(find(opcode, opcode+24, cmd)-opcode);
    bitset<3> rD(d);
    bitset<3> rA(a);
    cout << dec_to_bin << "0" << rD << rA;
    if (dec_to_bin.to_string()[4]=='0') {
        bitset<3> rB(c_or_b);
        cout << rB << "0";
    }else{
        bitset<4> C(c_or_b);
        cout << C;
    }
    cout << "\n";
    return;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    cin >> n;
    for (int i=0; i<n; i++) {
        solve();
    }
    return 0;
}