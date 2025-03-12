#include <iostream>
using namespace std;

const int INF = 1e9;

int main() {
	ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m, va, vb;
    cin >> n >> m;

    int dist[100][100];
    for (int i=0; i<n; i++){
        for (int j=0;j<n;j++){
            if(i!=j){
                dist[i][j]=INF;
            }
        }
    }

    for (int i=0;i<m;i++){
        cin >> va >> vb;
        dist[va-1][vb-1]=1;
        dist[vb-1][va-1]=1;
    }
    for (int m=0;m<n;m++){
        for (int s=0;s<n;s++){
            for(int e=0;e<n;e++){
                if (dist[s][e] > dist[s][m]+dist[m][e]){
                    dist[s][e] = dist[s][m]+dist[m][e];
                }
            }
        }
    }
    int ans, s, e;
    ans=INF;
    for (int i=0;i<n;i++){
        for (int j=0;j<n;j++){
            if(i==j)continue;
            int temp=0;
            for (int k=0;k<n;k++){
                temp+=min(dist[i][k], dist[j][k]);
            }
            if(ans>temp){
                ans = temp;
                s=i;
                e=j;
            }
        }
    }
    cout << s+1 << " " << e+1 << " " << ans*2;
	return 0;
}