package main

import "fmt"

func main() {
	// Variable assignment with specific type
	var a int = 5
	var b float32 = 4.32
	const pi float64 = 3.1415139475

	// Variable assignment with auto type
	c := 1

	// Variable reassignment (should be same type as first assignment)
	c = 5

	// Multiple variables assignment
	var (
		d = "hello"
		e = "there"
	)
	f, g := 14, 15

	fmt.Println(a)
	fmt.Println(b)
	fmt.Println(pi)
	fmt.Println(c)
	fmt.Println(d)
	fmt.Println(e)
	fmt.Println(f)
	fmt.Println(g)
}
