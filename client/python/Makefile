proto:
	@python -m grpc_tools.protoc -I../../protos --python_out=services/ --grpc_python_out=services/ ../../protos/task.proto
	@touch services/__init__.py

dep:
	@pip install -r requirements.txt

run:
	@env/bin/python app.py
