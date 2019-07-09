proto:
	@protoc -I../../protos --go_out=plugins=grpc:services/ ../../protos/*.proto

dep:
	@dep ensure

run:
	@go run cmd/main.go