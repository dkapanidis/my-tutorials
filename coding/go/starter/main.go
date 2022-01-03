package main

import (
	"flag"

	_ "go-starter/docs"
	"go-starter/pkgs/routers"
)

// @title Golang Starter
// @version 1.0.0
// @description Golang Starter.
// @termsOfService http://swagger.io/terms/

// @contact.name API Support

// @license.name MIT

// @BasePath /api/
func main() {
	r := routers.SetupRouter()

	addr := flag.String("address", "localhost:8080", "server address (default: 'localhost:8080')")
	flag.Parse()

	r.Run(*addr)
}
