// 인터페이스 인덱스
// 인덱스 시그니처

// 배열

interface Fruits {
    [item: number] : string
}

const fruits: Fruits = ["apple", "kiwi", "peach"]
console.log(fruits[1])
// 인덱싱 가능

// 객체
interface User {
    // [key: string] : unknown
    // unknown: 모든 값 허용
    name: string
    age: number
}

const kim: User = {
    name: "kim",
    age: 22
}

kim["isValid"] = true

// 확장, 상속 가능 ( extends )
// 속성 중복시 타입 맞춰주기.
// 같은 이름 다른 속성으로 여러 개 생성 가능

interface FullName {
    firstName: string
    lastName: string
}
interface FullName {
    middleName: string
    lastName: string
}
const fullName: FullName = {

}




