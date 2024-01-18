import { User, getFulName } from "./user";

const kim: User = {
  //   name: "kimbob",
  firstName: "kim",
  lastName: " bob",
  age: 12,
  isValid: true,
};
const fulName = getFulName(kim);

console.log(fulName);
console.log(kim.isValid);
