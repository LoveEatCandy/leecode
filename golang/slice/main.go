package main

import "fmt"

func main() {
	a := []int{1, 2, 3, 4, 5}
	b := a[:3]
	c := append(b, 100)
	fmt.Println(a) // [1 2 3 100 5]
	fmt.Println(b) // [1 2 3]
	fmt.Println(c) // [1 2 3 100]
}
