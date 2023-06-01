// abstract class provide blueprint for regular classes, cannot create object of abstract classes
// abstract methods needs to be redefined in extended classes, regular methods can be used directly or redefined on extended classes objects
abstract class Organism {
  constructor(
  public species: string,
  public sex: 'male' | 'female' | 'hermaphrodite'
  ){}

  born(): void {
    console.log("There's a new born!")
  }
  abstract reproduce(newBorn: number): number
}

class Animal extends Organism{
  constructor(
    public species: string,
    public sex: 'male' | 'female' | 'hermaphrodite',
    public age: number
  ){
    super(species, sex);
  }

  reproduce(newBorn: number): number {
    return newBorn + 1;
  }
}

const Pal = new Animal('dog', 'male', 1)
Pal.born(); // expect console.log
console.log(Pal.reproduce(3)); //expect return = 4