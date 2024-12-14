package main

import (
	"bufio"
	"os"
	"strings"
)

func check(err error) {
	if err != nil {
		panic(err)
	}
}

func readInput() ([]int, []int) {
	file, err := os.OpenFile("./input.txt", os.O_RDONLY, 0644)
	check(err)
	defer file.Close()

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {

		numbers := strings.Fields(scanner.Text())
		println(numbers)

	}

	return nil, nil
}

func main() {

	readInput()
}
