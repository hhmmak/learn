package main

import (
	"fmt"
	"strings"
)

func main() {

	fmt.Println("Enter a string:")
	var str string
	fmt.Scan(&str)

	strLower := strings.ToLower(str)

	containsIN := true
	containsA := false
	lastIdx := len(strLower) - 1

	for idx, r := range strLower {
		switch idx {
		case 0:
			if r != 'i' {
				containsIN = false
			}
		case lastIdx:
			if r != 'n' {
				containsIN = false
			}
		default:
			if r == 'a' {
				containsA = true
			}
		}
	}

	if containsA && containsIN {
		fmt.Println("Found!")
	} else {
		fmt.Println("Not Found!")
	}
}
