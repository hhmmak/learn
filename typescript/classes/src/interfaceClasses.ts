interface Animal {
  species: string
  sex: 'male' | 'female' | 'hermaphrodite'
  age: number
}

interface Owner {
  name: string,
  address: string
}

interface AnimalInteraction {
  feed(): void
  play(): void
}

// class implementing an interface must at least include all properties in exactly same properties
class WildAnimal implements Animal {
  constructor(
    public species: string,
    public sex: 'male' | 'female' | 'hermaphrodite',
    public age: number,
    public location: string
  ){}
}

class Pet implements Animal, Owner, AnimalInteraction {
  constructor(
    public species: string,
    public sex: 'male' | 'female' | 'hermaphrodite',
    public age: number,
    public name: string,
    public address: string
  ){}

  feed(): void {
    console.log('Pet is full')
  }

  play(): void{
    console.log('Pet is happy')
  }
}