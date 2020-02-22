proto:
	@protoc -I../../protos --go_out=plugins=grpc:services/ ../../protos/*.proto

dep:
	@go mod tidy

run:
	@go run cmd/main.go