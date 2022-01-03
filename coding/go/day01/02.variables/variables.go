package main

import "fmt"

func main() {
	// A constant is a variable with a value that can't be changed
	const pi float64 = 3.14159265359
	// You can declare multiple variables like this
	var (
		varA = 2
		varB = 3
	)
	fmt.Println(varA, varB)

	// Strings are a series of characters between " or `
	var Name string = "John Wick"

	// Get string length
	fmt.Println(len(Name))
}
