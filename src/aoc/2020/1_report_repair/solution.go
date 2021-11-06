package main

import (
	"files"
	"fmt"
)

func ReportRepair(input []int) int {
	diffSet := make(map[int]struct{})
	total := 2020

	for _, n := range input {
		diff := total - n
		// check diff already exists in the set
		// if found that is our match
		if _, exists := diffSet[n]; exists {
			return diff * n
		}

		diffSet[diff] = struct{}{}
	}
	return 0
}

func main() {
	input := files.ReadFileBuffer("data.txt")
	resp := ReportRepair(input)
	fmt.Println("Total mul:", resp)
}
