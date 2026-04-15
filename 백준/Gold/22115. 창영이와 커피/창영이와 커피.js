let input = require("fs").readFileSync('/dev/stdin').toString();
input = input.split("\n")
    
const [n, k] = input[0].split(" ").map(Number)
const dp = new Array(k+1).fill(1e9)
dp[0]=0

input = input[1].split(" ").map(Number)
for (let i = 0; i < n; i++) {
    let now = input[i]
    for (let j = k; j>=now; j--) {
        if(dp[j-now] === 1e9) continue
        dp[j]=Math.min(dp[j],dp[j-now]+1)
    }
    if (now<=k){
        dp[now]=1
    }
}

console.log(dp[k]===1e9?-1:dp[k])