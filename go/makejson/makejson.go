package main

import (
	"encoding/json"
	"fmt"
)

func main() {
	type person struct {
		name    string
		address string
	}

	var p person
	fmt.Println("Enter name:")
	fmt.Scan(&p.name)
	fmt.Println("Enter address:")
	fmt.Scan(&p.address)

	personMap := map[string]string{
		"name":    p.name,
		"address": p.address,
	}

	personJson, _ := json.Marshal(personMap)
	fmt.Println(string(personJson))
}
