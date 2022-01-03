package main

import "fmt"

func main() {
	x := 5

	fmt.Println(x)
	fmt.Println(&x)

	changeValuePassByValue(x) // pass by value
	fmt.Println(x)            // Prints 10

	changeValuePassByRef(&x) // pass by reference
	fmt.Println(x)           // prints 7
}

func changeValuePassByValue(x int) {
	x = 7
}

func changeValuePassByRef(x *int) {
	*x = 7
}
