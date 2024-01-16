
const tr = document.querySelector('#status-table > tbody > tr')
const tbody  = document.querySelector('#status-table > tbody')

// for(let i=0; i<9; i++){
//     console.log(tr)
//     console.log(tr[i])
// }
// console.log(tr)
// const problemNum = document.querySelector('#status-table > tbody > tr :nth-child(3)')
// console.log(problemNum)
// // 링크 타고 문제 내용 가져오기
// const result = document.querySelector('#status-table > tbody > tr :nth-child(4) > span')
// console.log("result : ", result.innerHTML)
// if (result.text === "맞았습니다!!"){
//     console.log("correct")
// }
// // 메모리
// const memory = document.querySelector('#status-table > tbody > tr :nth-child(5)')
// console.log("memory : ", memory)
// // 시간
// const time = document.querySelector('#status-table > tbody > tr :nth-child(6)')
// console.log("time : ", time);
// // 언어
// const language = document.querySelector('#status-table > tbody > tr :nth-child(7)')
// console.log("language : ", language)
// // 코드길이
// const length = document.querySelector('#status-table > tbody > tr :nth-child(8)')
// console.log("length :", length)
// // console.log(tbody.rows)

const data = {
    problemNum : document.querySelector('#status-table > tbody > tr :nth-child(3)'),
    result :  document.querySelector('#status-table > tbody > tr :nth-child(4) > span').innerHTML,
    memory : document.querySelector('#status-table > tbody > tr :nth-child(5)'),
    time : document.querySelector('#status-table > tbody > tr :nth-child(6)'),
    language : document.querySelector('#status-table > tbody > tr :nth-child(7)'),
    length : document.querySelector('#status-table > tbody > tr :nth-child(8)')
}
// console.log(tr.nth-child(3))
console.log(data)