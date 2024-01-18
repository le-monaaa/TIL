export interface User {
  firstName: string;
  lastName: string;
  age: number;
  isValid: boolean;
}

export function getFulName(user: User) {
  return `${user.firstName} ${user.lastName}`;
}
