interface Pet {
  species: string
  sex: 'male' | 'female' | 'hermaphrodite'
  age: number
}

interface Owner {
  name: string,
  address: string
}

interface PetInteraction {
  feed(): void
  play(): void
}

// class implementing an interface must at least include all properties in exactly same properties
class StorePet implements Pet {
  constructor(
    public species: string,
    public sex: 'male' | 'female' | 'hermaphrodite',
    public age: number,
    public location: string
  ){}
}

class HomePet implements Pet, Owner, PetInteraction {
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