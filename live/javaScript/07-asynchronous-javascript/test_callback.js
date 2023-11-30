
setTimeout(() => {
   console.log("1. 물을 끓인다.") 
   setTimeout(() => {
    console.log("2. 면과 스프를 넣는다.")
    setTimeout(() => {
       console.log("3. 계란을 넣는다") 
    }, 1000);
   }, 2000);
}, 3000);

// 이처럼 callback함수로 작성하면 indent level이 깊어질 수 밖에 없다.