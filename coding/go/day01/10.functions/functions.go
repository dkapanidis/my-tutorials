package main

import "fmt"

func main() {
	x, y := 5, 6

	fmt.Println(add(x, y)) // prints: 11

	fmt.Println(factorial(x)) // ( factorial(5) = 5x4x3x2x1 ) prints: 120
}

func add(num1, num2 int) int {
	return num1 + num2
}

func factorial(num int) int {
	if num == 0 {
		return 1
	}
	return num * factorial(num-1)
}
