package main

import "fmt"

func main() {
	rect1 := Rectangle{height: 10, width: 5}
	rect2 := Rectangle{10, 5}

	fmt.Println(rect1.height) // returns: 10
	fmt.Println(rect1.width)  // returns: 5
	fmt.Println(rect2)        // returns {10, 5}
	fmt.Println(rect1.area()) // returns: 50
}

// Rectangle a rectangle with dimensions
type Rectangle struct {
	height float64
	width  float64
}

func (rect *Rectangle) area() float64 {
	return rect.height * rect.width
}
