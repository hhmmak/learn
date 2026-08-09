package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

type name struct {
	fname string
	lname string
}

func main() {

	nameSlice := make([]name, 0, 10)

	var fileName string
	fmt.Println("Enter file name:")
	fmt.Scan(&fileName)

	file, err := os.Open(fileName)
	if err != nil {
		fmt.Println("Cannot open file: ", err)
		return
	}

	defer file.Close()

	scanner := bufio.NewScanner(file)

	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading file:", err)
		return
	}

	for scanner.Scan() {
		line := strings.TrimSpace(scanner.Text())

		parts := strings.Fields(line)
		nameSlice = append(nameSlice, name{
			fname: parts[0],
			lname: parts[1],
		})
	}

	for _, n := range nameSlice {
		fmt.Printf("%s %s\n", n.fname, n.lname)
	}
}
