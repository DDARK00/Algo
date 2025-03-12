#include <iostream>

int main() {
    std::string name,ans;
    int age, w;
    while(true){
        std::cin >> name >> age >> w;
        if(name=="#")break;
        if(age>17 || w>=80){
            ans = "Senior";
        }else{
            ans = "Junior";
        }
        std::cout << name << " " << ans << std::endl;
    }
    return 0;
}