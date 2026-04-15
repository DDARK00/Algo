#include <iostream>
 
int main() {
    int t;
    std::cin>>t;
    std::string a, b;
    for (int i=0; i<t; i++) {
        std::cin>>a>>b;
        std::string ans="OK \n";
        for(int j=0;j<a.size();j++){
            if(a[j]!=b[j]){
                ans = "ERROR \n";
                break;
            }
        }
        std::cout << ans;
    }
    return 0;
}