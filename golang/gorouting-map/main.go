package main

import (
	"math/rand"
	"sync"
)

const N = 10

func main() {
	m := make(map[int]int) // 加锁 或者 sync.Map
	// m := new(sync.Map)
	wg := &sync.WaitGroup{}
	// mutex := &sync.Mutex{}
	wg.Add(N)
	for i := 0; i < N; i++ {
		go func() {
			defer wg.Done()
			// mutex.Lock()
			m[rand.Int()] = rand.Int()
			// mutex.Unlock()
		}()
	}
	wg.Wait()
	println(len(m))
}
