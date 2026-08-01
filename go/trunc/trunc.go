package main

import (
	"fmt"
)

func main() {

	var floatNum float64
	fmt.Println("Enter a float number:")
	fmt.Scan(&floatNum)

	intNum := int(floatNum)

	fmt.Println(intNum)
}
