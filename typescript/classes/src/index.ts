// classic way to define class
class UserTraditional {
  // define type for properties ahead of constructor
  email: string;
  name: string;
  city: string = ""
  private age: number;
  readonly adult: boolean = true

  // define type for params
  constructor(email: string, name: string, age: number){
    this.email = email;
    this.name = name;
    this.age = age;
  }
}

// more efficient way to define class
class User {
  
  city: string = "";
  readonly adult: boolean = this.age >= 19;
  private _friendsCount: number = 0;
  // define type and public/private for properties same time as parameter, shorthand
  constructor(
    public email: string, 
    public name: string, 
    private age: number){
  }

  //define public/private methods
  consoleLogUserAdult(){
    console.log(`User: ${this.email}, ${this.name}, ${this.city}, adult: ${this.adult}`)
  }
  private consoleLogUserAge(){
    console.log(`User: ${this.email}, ${this.name}, ${this.city}, age: ${this.age}`)
  }

  //getters and setters for private methods
  get friendsCount(): number{
    return this._friendsCount;
  }
  // no return type statement required for setters
  set friendsCount(changeNum){
    if (changeNum > this._friendsCount){
      throw new Error("Cannot have less than 0 friends")
    }
    this._friendsCount += changeNum;
  }
}

const user1 = new User("abc@mail.com", "user1", 21)
user1.city = 'New York';
console.log(user1.adult)