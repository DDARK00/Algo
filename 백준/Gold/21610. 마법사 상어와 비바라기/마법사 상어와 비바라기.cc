#include <iostream>
#include <vector>
using namespace std;

int n, m;
vector<vector<int>> grid(50, vector<int>(50));

void init() {
    cin >> n >> m;
    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            cin >> grid[i][j];
        }
    }
}

int d, s;
vector<pair<int,int>> delta_xy={{0,-1},{-1,0},{0,1},{1,0}}; // 0 2 4 6
vector<pair<int,int>> delta_z={{-1,-1},{-1,1},{1,1},{1,-1}}; // 1 3 5 7
vector<pair<int,int>> cloud;
vector<pair<int,int>> moved_cloud;
vector<int> copyed_water; // 물복사용

vector<vector<int>> chk(50, vector<int>(50,-1)); // 2배수 체크 0비온다 1구름사라짐
void solve() {
    // 0. (N, 1), (N, 2), (N-1, 1), (N-1, 2)에 비구름
    cloud.push_back({n-1,0});
    cloud.push_back({n-1,1});
    cloud.push_back({n-2,0});
    cloud.push_back({n-2,1});
    // 1. 구름 이동
    // 2. 비온다
    // 3. 구름 사라짐
    // 4. 2해당되는 칸에 물복사
    // 5. 물2 이상은 구름, 물-2, 3의 칸은 해당안됨
    bool flag;
    for (int turn=0; turn<m; turn++) {
        cin >> d >> s; // 구름 이동, d방향으로 s칸
        d-=1;
        flag=d%2; // 1대각 0상하좌우
        d/=2;
        // 구름 이동
        for (auto k : cloud) {
            auto [x,y]=k;
            auto [dx,dy]=flag?delta_z[d]:delta_xy[d];
            int nx=((x+30*n)+dx*s)%n; // s50 n2
            int ny=((y+30*n)+dy*s)%n;
            moved_cloud.push_back({nx,ny});
            // cout << "이동한 좌표 :" << nx << " / " << ny <<"\n";
            // 비온다
            grid[nx][ny]++;

            // 구름 사라짐
            // 좌표
            chk[nx][ny]=turn;
        }
        // 물복사
        for (auto k : moved_cloud) {
            auto [x,y]=k;
            int added=0;
            for (auto d : delta_z) { // 대각
                auto [dx,dy]=d;
                if (x+dx>=0&&x+dx<n&&y+dy>=0&&y+dy<n) {
                    added+=grid[x+dx][y+dy]>0;
                }
            }
            copyed_water.push_back(added);
        }

        // 물복사 적용
        for (int i=0; i<moved_cloud.size(); i++) {
            auto [x,y]=moved_cloud[i];
            grid[x][y]+=copyed_water[i];
            // cout << "x :" << x << " y :" << y <<" 에 증가 :" <<copyed_water[i]<<"\n";
        }

        cloud={};
        // 새로운 구름 생성
        for (int i=0; i<n; i++) {
            for (int j=0; j<n; j++) {
                if (grid[i][j]>1 && chk[i][j]!=turn) {
                    cloud.push_back({i,j});
                    grid[i][j]-=2;
                }
            }
        }
        moved_cloud={};
        copyed_water={};
        // cout << "새로운 구름 : " << cloud.size() << "개 \n";
        // for (auto k : cloud) {
        //     auto [x,y]=k;
        //     cout << "x :" <<x<<"  / y :"<<y<<"\n";
        // }
        // for (int i=0; i<n; i++) {
        //     for (int j=0; j<n; j++) {
        //         cout << grid[i][j];
        //     }
        //     cout << "\n";
        // }
        // cout << "\n";
        
    } // 이동 끝
}

void print() {
    int answer=0; // 100+4*100 *2500
    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            answer+=grid[i][j];
        }
    }

    cout << answer << "\n";
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    init();
    solve();
    print();
    return 0;
}