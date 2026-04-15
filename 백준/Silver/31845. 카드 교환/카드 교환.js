let input = require("fs").readFileSync('/dev/stdin').toString();
input = input.split("\n")
const [n, m] = input[0].split(" ").map(Number)
const cards = input[1].split(" ").sort((a,b)=>b-a).map(Number)
let answer = 0, i = 0
class Deque {
    constructor() {
        this.items = {}
        // front는 가장 낮은 인덱스, back은 다음 삽입될 가장 높은 인덱스+1을 가리킴
        this.front = 0
        this.back = 0
    }

    get length() {
        return this.front - this.back;
    }

    isEmpty() {
        return this.length === 0;
    }

    push_front(data) {
        this.front--
        this.items[this.front] = data
    }

    push_back(data) {
        this.items[this.back] = data
        this.back++
    }

    pop_front() {
        if (this.isEmpty()) {
            return undefined
        }
        const result = this.items[this.front]
        delete this.items[this.frint]
        this.front++
        return result
    }

    pop_back() {
        if (this.isEmpty()) {
            return undefined
        }
        this.back--
        const result = this.items[this.back]
        delete this.items[this.back]
        return result
    }

    get get_front(){
        if (this.isEmpty()) {
            return undefined
        }
        return this.items[this.front]
    }

    get get_back(){
        if (this.isEmpty()) {
            return undefined
        }
        return this.items[this.back-1]
    }
}

const dq = new Deque()
for (let num of cards) {
    dq.push_back(num)
}
// 그냥 덱 한번 만들어보고 싶었음
while (true) {
    if (i===m || i===n || dq.isEmpty()) {
        break
    }
    if (dq.get_front>0) {
        answer+= dq.pop_front()
        dq.pop_back()
    }else{
        break
    }
    i++
}
console.log(answer)