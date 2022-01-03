package main

import "fmt"

func main() {
	StudentAge := make(map[string]int)

	StudentAge["John"] = 23
	StudentAge["Bob"] = 27
	StudentAge["Anna"] = 21
	StudentAge["Alice"] = 19
	StudentAge["Carl"] = 42
	StudentAge["Maria"] = 22

	fmt.Println(StudentAge["maria"]) // not found (case-sensitive) returns: 0
	fmt.Println(StudentAge["Maria"]) // found returns: 22
	fmt.Println(len(StudentAge))     // returns 6 (number of elements)

	superhero := map[string]map[string]string{
		"Superman": {
			"RealName": "Clar Kent",
			"City":     "Metropolis",
		},
		"Batman": {
			"RealName": "Bruce Wayne",
			"City":     "Gotham City",
		},
	}

	if temp, hero := superhero["Superman"]; hero {
		fmt.Println(temp["RealName"], temp["City"], hero)
	}
}
