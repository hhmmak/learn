package main

import (
	"fmt"
	"slices"
	"strconv"
)

func main() {

	sli := make([]int, 0, 3)

	var inpt string

	fmt.Println("Enter a number (enter 'X' to exit):")
	fmt.Scan(&inpt)

	for inpt != "X" {
		inptInt, _ := strconv.Atoi(inpt)
		sli = append(sli, inptInt)
		slices.Sort(sli)
		fmt.Println(sli)
		fmt.Println("Enter a number (enter 'X' to exit):")
		fmt.Scan(&inpt)
	}
}
