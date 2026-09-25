# output_pb2.py (Dynamic Generator - No protoc needed)
from google.protobuf import descriptor_pb2
from google.protobuf import descriptor_pool
from google.protobuf import message_factory

def _build_garena_420():
    file_proto = descriptor_pb2.FileDescriptorProto()
    file_proto.name = 'output.proto'
    file_proto.syntax = 'proto3'

    msg = file_proto.message_type.add()
    msg.name = 'Garena_420'

    # Token field (1)
    f = msg.field.add()
    f.name = 'token'
    f.number = 1
    f.label = descriptor_pb2.FieldDescriptorProto.LABEL_OPTIONAL
    f.type = descriptor_pb2.FieldDescriptorProto.TYPE_STRING

    # Fields 2 to 30
    for i in range(2, 31):
        f = msg.field.add()
        f.name = f'field_{i}'
        f.number = i
        f.label = descriptor_pb2.FieldDescriptorProto.LABEL_OPTIONAL
        f.type = descriptor_pb2.FieldDescriptorProto.TYPE_STRING

    pool = descriptor_pool.DescriptorPool()
    pool.Add(file_proto)
    
    try:
        return message_factory.GetMessageClass(pool.FindMessageTypeByName('Garena_420'))
    except AttributeError:
        factory = message_factory.MessageFactory(pool)
        return factory.GetPrototype(pool.FindMessageTypeByName('Garena_420'))

Garena_420 = _build_garena_420()