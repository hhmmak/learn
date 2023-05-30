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
  
  // define type and public/private for properties same time as parameter, shorthand
  constructor(
    public email: string, 
    public name: string, 
    private age: number){
  }
}

const user1 = new User("abc@mail.com", "user1", 21)
user1.city = 'New York';
console.log(user1.adult)