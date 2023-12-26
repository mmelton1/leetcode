package main

import "fmt"

func findDestinationCity(paths [][]string) string {
	for _, path := range paths {
		fmt.Println("Path1: ", path)
		fmt.Println("Path1[0]: ", path[0])
		fmt.Println("Path1[1]: ", path[1])
		found := false
		for _, otherPath := range paths {
			fmt.Println("Path2: ", path)
			fmt.Println("OthPath2[0]: ", path[0])
			fmt.Println("OthPath2[1]: ", path[1])
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
