#include <iostream>
using namespace std;

int main() {
    int n, m, u, v, i, j;
    cin >> n >> m >> u >> v;

    char texture[n][m];
    char text[u][v];
    int k=1;

    string s, type;
    for (i=0; i<min(n,u); i++) {
        cin >> s;
        for (int j=0; j<min(m,v); j++){
            text[i][j]=s[j];
        }
    }
    cin >> type;
    if (type=="clamp-to-edge"){
        for(i=0;i<n;i++){
            for(j=0;j<m;j++){
                texture[i][j]=text[min(i,u-1)][min(j,v-1)];
            }
        }
    }else if (type=="repeat"){
        for (i=0;i<n;i++){
            for (j=0;j<m;j++){
                texture[i][j]=text[i%u][j%v];
            }
        }
    }else{
        int p,q;
        for(i=0;i<n;i++){
            for(j=0;j<m;j++){
                if((j/v)%2){
                    q=v-(j%v)-1;
                }else{
                    q=j%v;
                }
                if((i/u)%2){
                    p=u-(i%u)-1;
                }else{
                    p=i%u;
                }
                texture[i][j]=text[p][q];
            }
        }
    }

    for (i=0;i<n;i++){
        for (j=0;j<m;j++){
            cout<<texture[i][j];
        }
        cout<<"\n";
    }
    return 0;
}