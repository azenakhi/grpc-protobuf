# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from services import task_pb2 as task__pb2


class TaskServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.List = channel.unary_unary(
        '/services.TaskService/List',
        request_serializer=task__pb2.Void.SerializeToString,
        response_deserializer=task__pb2.TaskList.FromString,
        )
    self.Add = channel.unary_unary(
        '/services.TaskService/Add',
        request_serializer=task__pb2.Task.SerializeToString,
        response_deserializer=task__pb2.Task.FromString,
        )


class TaskServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def List(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Add(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_TaskServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'List': grpc.unary_unary_rpc_method_handler(
          servicer.List,
          request_deserializer=task__pb2.Void.FromString,
          response_serializer=task__pb2.TaskList.SerializeToString,
      ),
      'Add': grpc.unary_unary_rpc_method_handler(
          servicer.Add,
          request_deserializer=task__pb2.Task.FromString,
          response_serializer=task__pb2.Task.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'services.TaskService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
