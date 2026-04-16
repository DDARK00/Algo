let input = require("fs").readFileSync('/dev/stdin').toString();
input = input.split("\n")
const n = Number(input[0])
const sizes = input[1].split(" ")
// S, M, L, XL, XXL, XXXL
input = input[2].split(" ")
const t = Number(input[0])
const p = Number(input[1])

let tGrp = 0
for (let size of sizes) {
    tGrp += Math.ceil(size/t)
}
console.log(tGrp)
console.log(Math.floor(n/p),n%p)