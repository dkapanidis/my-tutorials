package main

import "fmt"

func main() {
	// normal loop
	for i := 1; i < 10; i++ {
		fmt.Println(i)
	}

	// while style loop
	i := 1
	for i < 10 {
		fmt.Println(i)
		i++
	}

	// nested loop
	for i := 1; i < 10; i++ {
		for j := 1; j < i; j++ {
			fmt.Printf("*")
		}
		fmt.Println()
	}
}
