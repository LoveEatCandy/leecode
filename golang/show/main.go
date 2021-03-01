package main

import (
	"fmt"
)

func main() {
	if a := 0; a <= 5 {
		fmt.Println(a)
	}

	for b := 0; b <= 5; b++ {
		fmt.Println(b)
	}

	l := []int{1, 2, 3, 4, 5}
	for i, num := range l {
		fmt.Println(i, num)
	}
}
