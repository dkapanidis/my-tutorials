package main

import "fmt"

func main() {
	var EvenNum [5]int
	EvenNum[0] = 0
	EvenNum[1] = 2
	EvenNum[2] = 4
	EvenNum[3] = 6
	EvenNum[4] = 8

	fmt.Println(EvenNum[2]) // prints: 4

	OddNum := [5]int{0, 1, 3, 5, 7}
	fmt.Println(OddNum[2]) // prints: 3

	for _, value := range OddNum {
		fmt.Println(value)
	}

	numSlice := []int{5, 4, 3, 2, 1}
	sliced := numSlice[3:5]
	fmt.Println(sliced)        // prints: [2, 1]
	fmt.Println(numSlice[3:])  // prints: [2, 1]
	fmt.Println(numSlice[:])   // prints: [5, 4, 3, 2, 1]
	fmt.Println(numSlice[0:1]) // prints: [5]

	slice2 := make([]int, 5, 10)
	copy(slice2, numSlice) // copies numSlice to slice2
	fmt.Println(slice2)    // prints [5, 4, 3, 2, 1]

	slice3 := append(numSlice, 3, 0, -1)
	fmt.Println(slice3) // prints [5, 4, 3, 2, 1, 3, 0, -1]
}
