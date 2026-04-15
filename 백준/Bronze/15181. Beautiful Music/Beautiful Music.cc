#include <iostream>
#include <vector>
using namespace std;

int main() {
    string notes;
    while (true){
        cin >> notes;
        if (notes=="#")break;
        char before = notes[0]-'A';
        bool chk=true;
        for (int i=1;i<notes.size();i++){
            int diff=((notes[i]-'A')-before)%7;
            if(diff<0){
                diff+=7;
            }
            if (diff!=2 && diff!=4 && diff !=6){
                chk=false;
                break;
            }
            before = notes[i]-'A';
        }
        if(chk){
            cout<<"That music is beautiful. \n";
        }else{
            cout<<"Ouch! That hurts my ears. \n";
        }
    }
    return 0;
}