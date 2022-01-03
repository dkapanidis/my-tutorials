package main

import "fmt"

func main() {
	x := 10

	changeValue(&x) // pass by reference
	fmt.Println(x) // prints 7
}

func changeValue(x *int) {
	*x = 7
}
