// initiate 'number'-type variable age to 20
let username: string = 'johndoe';
let age: number = 20;
let vip: boolean = true;
//nullable types
let followingId: number | null = 12; //variable can either be a number or null value
let birthday: Date | undefined = undefined; //variable can either be a Date object or undefined
let remark; //'any'-type variable, can first be 10 then true then 'word-string'
// declare a tuple
let savingsAccount: [string, number] = ['678435910', 123_456] // 123_456 === 1234556; typescript allows use of _ to make number easier to read
//declare array that consist of only numbers
let numbers: number[] = [1, 2, 3]
//declare enum
const enum Size {Small = '360px', Medium = '480px', Large = '600px'}
let myMobileSize: Size = Size.Large //expected console.log = 600px
//declare literal type
type BloodType = 'A' | 'B' | 'O' | 'AB';
let myBloodType: BloodType = 'A'
//union type
type width = {
  widthNum: number
}
type length = {
  lengthNum: number
}
type dimension = width & length;


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
  userMethod?: (date: Date) => void
  accountNumber: string | number
  friends: string[]
}
let user1: User = {
  id: 1,
  username: 'johnDoe',
  userMethod: (date: Date) => console.log(date),
  accountNumber: 980657423,
  friends: ["bobK", "janeL", "pascalT"]
}

//operational chaining
const getUser = (id: number) : User | null | undefined => {
  return id === 1? user1 : undefined;
}
let user2 = getUser(0); //expect : user2 === undefined
console.log(user2?.username) //operational property access operator; runs only if user2 isn't a null/undefined
console.log(user2?.friends?.[5])  //operational element access operator
user2?.userMethod?.(new Date);
