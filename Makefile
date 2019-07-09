.PHONY: server
server:
	@protoc -Iproto/ --go_out=plugins=grpc:server/services/ proto/*.proto

.PHONY: client
client:
	@protoc -Iproto/ --go_out=plugins=grpc:client/services/ proto/*.proto