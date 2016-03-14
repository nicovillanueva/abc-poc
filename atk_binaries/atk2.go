package main

import (
	"fmt"
	"flag"
	"os"
	"crypto/rand"
)

func main() {
	sPtr := flag.Bool("success", false, "Success or not")
	v := flag.Bool("verbose", false, "Printout shit message")
	flag.Parse()
	
	if (*v) {
		fmt.Println("Hello, I'm attacker 2. I print out a key if ran with --success, -1 otherwise")
	}

	if (*sPtr) {
		p, _ := rand.Prime(rand.Reader, 64)
		fmt.Println(p)
		os.Exit(0)
	} else {
		fmt.Println("-1")
		os.Exit(1)
	}
}
