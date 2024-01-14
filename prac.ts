

const el = document.querySelector("body")
el.textContent = "Hello, World"
// 에러 : el은 null 일 수 있다
// body 가 html에 존재하는지 ts는 알 수가 없다.
// 확실히 이게 있다고 단언할 수 있을 때 사용

const el1 = document.querySelector("body") as HTMLBodyElement
// queryselector로 찾은 "body"는 반드시 null이 아니고,
// html의 bodyelement가 될 것이다. 라고 단언

function getNumber(x:number | null | undefined) {
    return Number(x.toFixed(2))
}
getNumber(3.1231412)
getNumber(null)


function getNumber2(x:number | null | undefined) {
    return Number((x as number).toFixed(2))
}
// x에는 null 이 들어오지 않을 것이고 number일 것이다.
getNumber2(3.1231412)
getNumber2(null)


//

function getValue(x: string | number, isNumber: boo)