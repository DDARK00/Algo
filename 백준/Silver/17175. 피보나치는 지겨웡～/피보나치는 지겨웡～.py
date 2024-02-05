n = int(input())
dp = [0]*51 # 1 1 2 3 5 8 1이 없네
dp[0] = 1
dp[1] = 1
for i in range(2,51):
    dp[i] =(dp[i-2]+dp[i-1] +1)
 

print(dp[n]%1000000007)
# 수가 그냥 호출횟수 아냐?... 1로 리턴되니까...?
# 가 아니구나 0 1 일때 1번 호출
# 2일 때 1(0) 1(1)  + 1번 호출

'''
int fibonacci(int n) { // 호출
  if (n < 2) {
    return n;
  }  
  return fibonacci(n-2) + fibonacci(n-1);
}
'''