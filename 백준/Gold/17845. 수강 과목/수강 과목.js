let input = require("fs").readFileSync('/dev/stdin').toString();
input = input.split("\n")

const [n, k] = input[0].split(" ").map(Number)
// 10000 1000
let value, cost
const dp= new Array(n+1).fill(0)
for (let i=0;i<k;i++){
    [value, cost] = input[1+i].split(" ").map(Number)
    for(let j=n;j>=cost;j--){
        dp[j] = Math.max(dp[j], dp[j-cost]+value)
    }
}
console.log(dp[n])