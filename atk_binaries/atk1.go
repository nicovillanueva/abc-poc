package main

import (
	"fmt"
	"flag"
	"os"
)

func main() {
	sPtr := flag.Bool("success", false, "Success or not")
	v := flag.Bool("verbose", false, "Printout shit message")
	flag.Parse()

	if (*v) {
		fmt.Println("Hello, I'm attacker 1. I exit with 0 if ran with --success, 1 otherwise")
	}

	if (*sPtr) {
		if (*v) {
			fmt.Println("Success")
		}
		os.Exit(0)
	} else {
		if (*v) {
			fmt.Println("Failure")
		}
		os.Exit(1)
	}
}
