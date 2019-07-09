package main

import (
	"fmt"
	"log"
	"net"

	"google.golang.org/grpc"

	"github.com/azenakhi/grpc-protobuf/server/services"
)

func main() {
	taskService := services.TaskService{}
	srv := grpc.NewServer()
	services.RegisterTaskServiceServer(srv, taskService)
	listener, err := net.Listen("tcp", ":8080")
	if err != nil {
		log.Fatalf("could not listen to :8080 %v", err)
	}
	fmt.Println(srv.Serve(listener))
}
