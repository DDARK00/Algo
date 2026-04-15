let n, arr, s;
{
    let input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
    n=Number(input[0]);
    arr=input[1].split(" ").map(Number);
    s=Number(input[2]);
}


for (let i = 0; i < n; i++) {
    // 왼쪽부터 s(-cnt)이내에 가능한 가장 큰 수를 배치
    let target=0, idx=i;
    for (let j = 0; j < Math.min(n,s+1); j++) {
        if (target<arr[i+j]) {
            target=arr[i+j];
            idx=i+j;
        }
    }
    // console.log(target,idx," // ",Math.min(n,s))
    s-=idx-i;
    if (i!=idx) {
        arr.splice(i,0,arr[idx]);
        arr.splice(idx+1,1);
    }
}

console.log(...arr)