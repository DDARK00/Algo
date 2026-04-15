let input = require("fs").readFileSync('/dev/stdin').toString();
input = input.split("\n")

n = Number(input[0])
for (let i = 0; i < n; i++) {
    console.log(input[1+i].replaceAll("PO","PHO"))
}