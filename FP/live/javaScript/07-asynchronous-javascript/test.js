console.log("라면을 끓인다. (각 과정이 준비되는 데 1~3초 시간이 걸린다")

// 물을 끓는데 3초가 걸림
setTimeout(() => {
    console.log("1. 물을 끓인다.")
}, 3000);

// 스프랑 면을 넣는다
setTimeout(() => {
    console.log("2. 스프랑 면을 넣는다.")
}, 2000);

// 계란을 넣는다.
setTimeout(() => {
    console.log("3. 계란을 넣는다.")
}, 1000);

console.log("완성~!~!~!!!!~!~!")