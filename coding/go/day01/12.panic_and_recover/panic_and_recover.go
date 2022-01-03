package main

import "fmt"

func main() {
	fmt.Println(div(3, 0))
	fmt.Println(div(5, 3))
	demPanic()
}

func div(num1, num2 int) int {
	defer func() {
		fmt.Println("div Recovered: ", recover())
	}()
	solution := num1 / num2 // (This will panic if num2 is 0)
	return solution
}

func demPanic() {
	defer func() {
		fmt.Println("demPanic Recovered:", recover())
	}()
	panic("Paniced")
}
