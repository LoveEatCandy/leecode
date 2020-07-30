package main

import (
	"fmt"
)

func main() {
	defer func() {
		fmt.Println("1")
	}()
	defer func() {
		fmt.Println("2")
	}()
	defer func() {
		fmt.Println("3")
	}()

	panic("err") // 输出 3， 2， 1
	// os.Exit(0) // 直接退出进程
}
