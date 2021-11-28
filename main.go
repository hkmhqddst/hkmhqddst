package main

import (
	"fmt"
	"net/http"
)

func main() {
	http.HandleFunc("/student", ActionStudent)

	server := new(http.Server)
	server.Addr = ":9000"

	fmt.Println("server started at localhost:9000")
	server.ListenAndServe()
}
