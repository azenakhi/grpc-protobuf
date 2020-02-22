import grpc
from services import task_pb2 
from services import task_pb2_grpc
import services

channel = grpc.insecure_channel('localhost:8080')

# create a stub (client)
stub = task_pb2_grpc.TaskServiceStub(channel)


l = stub.List(task_pb2.Void())

tasks = l.tasks

for i in range(len(tasks)):
    print(tasks[i])