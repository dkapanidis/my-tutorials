package main

import "fmt"

func main() {
	x := 10

	changeValue(x) // pass by value
	fmt.Println(x) // Prints 10
}

func changeValue(x int) {
	x = 7
}
