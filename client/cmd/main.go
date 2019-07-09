package main

import (
	"context"
	"fmt"
	"log"
	"os"

	"github.com/azenakhi/grpc-protobuf/client/services"

	"google.golang.org/grpc"
)

func main() {
	conn, err := grpc.Dial(":8080", grpc.WithInsecure())
	defer conn.Close()
	if err != nil {
		log.Fatalf("Don't connect to backend: %v", err)
		os.Exit(1)
	}
	client := services.NewTaskServiceClient(conn)
	tasks, err := client.List(context.Background(), &services.Void{})
	if err != nil {
		log.Fatalf("List is vide %v", err)
	}
	for _, task := range tasks.Tasks {
		fmt.Println(task)
	}
}
