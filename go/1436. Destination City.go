package main

import "fmt"

func findDestinationCity(paths [][]string) string {
	for _, path := range paths {
		found := false
		for _, otherPath := range paths {
			if path[1] == otherPath[0] {
				found = true
				break
			}
		}
		if !found {
			return path[1]
		}
	}

	return "" // Return an empty string if no destination city is found
}

func main() {
	paths1 := [][]string{
		{"London", "New York"},
		{"New York", "Lima"},
		{"Lima", "Sao Paulo"},
	}
	fmt.Println(findDestinationCity(paths1)) // Output: "Sao Paulo"
}
