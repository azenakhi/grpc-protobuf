proto:
	@python3.7 -m grpc_tools.protoc -I../../protos --python_out=services/ --grpc_python_out=services/ ../../protos/task.proto

dep:
	@pip3.7 install -r requirements.txt

run:
	@env/bin/python3.7 app.py
