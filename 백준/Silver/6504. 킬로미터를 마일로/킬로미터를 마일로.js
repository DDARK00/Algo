let input = require("fs").readFileSync('/dev/stdin').toString();
input = input.split("\n")
/*
F1 = 1
F2 = 2
Fn+1 = Fn + Fn-1 (n > 1)
*/
f=[]
f[0] = 1
f[1] = 2
for (let i = 2; f[i-1] <= 25000; i++){
    f[i] = f[i-2]+f[i-1]
}

const findCode = (target)=>{
    let code = ""
    let idx = f.length-1
    while (idx>0) {
        if (f[idx]<=target) {
            break
        }else{
            idx-=1
        }
    }

    for (; idx >= 0; idx--) {
        if (f[idx]<=target) {
            target-=f[idx]
            code+="1"
        }else{
            code+="0"
        }
    }
    return code
}

for (i = 0; i < input[0]; i++) {
    let num = Number(input[i+1])
    
    let code  = findCode(num)
    const doneCode = code.substr(0,code.length-1).split("").reverse().join("")
    // console.log(code,doneCode)
    let ans = 0
    for(j=0; j<doneCode.length;j++){
        if(doneCode[j] === "1"){
            ans+=f[j]
        }
    }
    console.log(ans)
}
// 어우 노드 번거롭네