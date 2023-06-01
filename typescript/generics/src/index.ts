const score: Array<number> = []   // same as const score: number[] = []; <> specifies Type
const names: Array<string> = []


// use <Type> to restrict the para and return data type to be the same; Type/T is just dummy variable such that all types = Type will be of same data type
function genericFuncOne<Type>(val: Type): Type{
  return val
}
function genericFuncTwo<T>(val: T): T{
  return val
}

// usage example
interface User{
  id: number
  username: string
}
genericFuncTwo<User>({id:0, username:"master"});  // expect return to be {id:0, username:"master"}

// generic arrow function and creating an extended arrow function
const genericFuncArrowArrToEle = <T,>(arr: T[]): T => {
  let idx = 0;
  //some operations
  return arr[idx]
}
const genericFuncArrowArrToArr = <T,>(arr: T[]): T[] => {
  return arr
}