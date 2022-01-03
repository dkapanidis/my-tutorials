package main

import "fmt"

func main() {
	defer firstRun() // It will execute last, after secondRun() function
	secondRun()
}

func firstRun() {
	fmt.Println("I executed first")
}

func secondRun() {
	fmt.Println("I executed second")
}
