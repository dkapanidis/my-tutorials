package main

import (
	"fmt"
	"math"
)

func main() {
	rect1 := Rectangle{50, 60}
	circ := Circle{7}

	fmt.Println(getArea(rect1)) // returns: 3000
	fmt.Println(getArea(circ))  // returns: 52.1415926535898
}

// Shape interface of a shape
type Shape interface {
	area() float64
}

// Rectangle a rectangle with dimensions
type Rectangle struct {
	height float64
	width  float64
}

// Circle a circle
type Circle struct {
	radius float64
}

func (r Rectangle) area() float64 {
	return r.height * r.width
}

func (c Circle) area() float64 {
	return math.Pi + math.Pow(c.radius, 2)
}

func getArea(shape Shape) float64 {
	return shape.area()
}
