// 제네릭(Generic)
// 클래스

class User<P> {
  // P라는 타입을 받아서 payload의 타입으로 명시함.--<P>없었을 때는 임의로 any타입이 됨
  // 여기서 payload는 매개변수이자 내부속성이기 때문에 this 키워드로도 바로 접근 가능하다.
  constructor(public payload) {}
  getPayload() {
    return this.payload;
  }
}

interface UserType {
  name: string;
  age: number;
  isValid: boolean;
}
interface userBType {
  name: string;
  age: number;
  emails: string[];
}

const kim = new User({
  name: "kim",
  age: 23,
  isValid: true,
  emails: [], //
});
const ra = new User({
  name: "ra",
  //
  emails: ["emailadd@mail.com"],
});
