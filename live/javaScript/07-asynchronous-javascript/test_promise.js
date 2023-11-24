/**
 손님이 분식점에서 라면을 주문했다--> 내가 만든 화면을 사용자가 요청함.
 라면 == 화면
 라면 재료 준비 == 화면을 보여주는 데 필요한 데이터들
 다 완성되면 서빙 == 다 완성되면 화면 보여주기

 promise의 세가지 상태
 대기(pending)- 이행하지도, 거부하지도 않은 초기 상태
 이행(fulfilled)- 연산이 성공적으로 완료됨
 거부(rejected)- 연산이 실패함

 promise object 사용법
 new Promise((resolve, reject) => {

    if(비동기작업 완료 조건){
        return resolve(value) // 비동기작업이 성공했을 때 리턴하고싶은 값이 있으면 value
    } else if (비동기작업 실패 조건) {
        return reject(value) // 비동기작업이 실패했을 때 리턴하고 싶은 값이 있으면 value
    }

    .then()과 .catch()는 Promise 객체에 사용하는 메서드.
 })
*/

// 물을 끓이는 함수. 3초 소요
const water = function (ramen) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
           console.log("1. 물을 끓인다") 
           ramen.push("물")
           return resolve(ramen) // 이 비동기 작업이 잘 끝났을 때 resolve 함수로 ramen 반환
            // return reject(ramen) // 거부 반환
    }, 3000);
    })
}

const soupAndNoodle = function(ramen) {
    return new Promise((resolve, reject)=> {
        setTimeout(() => {
            console.log("2. 스프와 면을 넣는다.")
            ramen.push("스프")
            ramen.push("면")
            return resolve(ramen)
        }, 2000);
    }) 
}

const egg = function(ramen) {
    return new Promise((resolve, reject)=> {
        setTimeout(() => {
            console.log("3. 계란을 넣는다.")
            ramen.push("계란")
            return resolve(ramen)
        }, 2000);
    }) 
}

const ramen = []

// axios로 요청을 보내고 server에서 성공적으로 실행되어서 응답을 보내면 then으로 보냄

// water가 끝나야 실행되는 .then 함수
water(ramen)
    .then((ramen) => {
        return soupAndNoodle(ramen)
    })
    .then((ramen) => {
        return egg(ramen)
    })
    // 중간 에러 발생 시 실행할 함수
    .catch((err)=> {
        console.log("라면을 끓이는 도중에 문제가 발생 : ", err)
    })
    .then(() => {
        console.log("라면 완성~!~!~!~!~!!~!~ : ", ramen)
    })

    // resolve, reject