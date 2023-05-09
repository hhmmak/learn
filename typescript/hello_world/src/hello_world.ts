// initiate 'number'-type variable age to 20
let username: string = 'johndoe';
let age: number = 20;
let vip: boolean = true;
let remark; //'any'-type variable, can first be 10 then true then 'word-string'
// declare a tuple
let savingsAccount: [string, number] = ['678435910', 123_456] // 123_456 === 1234556; typescript allows use of _ to make number easier to read
//declare array that consist of only numbers
let numbers: number[] = [1, 2, 3]
//declare enum
const enum Size {Small = '360px', Medium = '480px', Large = '600px'}
let myMobileSize: Size = Size.Large //expected console.log = 600px


//declare function with no return value
const printOnConsole = (content: any): void => {  //declare parameter with 'any'-type
  console.log("content = ", content)
}
//declare function with specified return data type
const helloWord = () : string => {
  return 'Hello World!';
}
//declare function with optional params, tsconfig: noUnusedLocals, noUnusedParameters, noImplicitReturns for error checking
const reduceAmount = (num: number, diff = 50) : number => {
  if (num >= diff)
    return num - diff;
  return 0;
}

//declare object, readonly keyword to set key as constant
let user: {
  readonly id: number,
  username: string
} = {
  id: 1,
  username: 'johnDoe'
}

//declare a 'type' variable to be resued, like a class; accountNumber can either be a string or number
type User = {
  readonly id: number,
  username: string,
  userMethod: (date: Date) => void
  accountNumber: string | number
}
let user1: User = {
  id: 1,
  username: 'johnDoe',
  userMethod: (date: Date) => console.log(date),
  accountNumber: 980657423
}

