package main

import "fmt"

func main() {
	age := 18

	// if else
	if age >= 18 {
		fmt.Println("you can van vote")
	} else {
		fmt.Println("you cannot vote")
	}

	// switch case
	switch age {
	case 16:
		fmt.Println("Prepare for college")
	case 18:
		fmt.Println("Don't run after girls")
	case 20:
		fmt.Println("Get yourself a job!")
	default:
		fmt.Println("Are you even alive?")
	}
}
