# my_pb2.py (Dynamic Generator - No protoc needed)
from google.protobuf import descriptor_pb2
from google.protobuf import descriptor_pool
from google.protobuf import message_factory

def _build_gamedata():
    file_proto = descriptor_pb2.FileDescriptorProto()
    file_proto.name = 'my.proto'
    file_proto.syntax = 'proto3'

    msg = file_proto.message_type.add()
    msg.name = 'GameData'

    fields = [
        ('timestamp', 1, descriptor_pb2.FieldDescriptorProto.TYPE_STRING),
        ('game_name', 2, descriptor_pb2.FieldDescriptorProto.TYPE_STRING),
        ('game_version', 3, descriptor_pb2.FieldDescriptorProto.TYPE_INT32),
        ('version_code', 4, descriptor_pb2.FieldDescriptorProto.TYPE_STRING),
        ('os_info', 5, descriptor_pb2.FieldDescriptorProto.TYPE_STRING),
        ('device_type', 6, descriptor_pb2.FieldDescriptorProto.TYPE_STRING),
        ('network_provider', 7, descriptor_pb2.FieldDescriptorProto.TYPE_STRING),
        ('connection_type', 8, descriptor_pb2.FieldDescriptorProto.TYPE_STRING),
        ('screen_width', 9, descriptor_pb2.FieldDescriptorProto.TYPE_INT32),
        ('screen_height', 10, descriptor_pb2.FieldDescriptorProto.TYPE_INT32),
        ('dpi', 11, descriptor_pb2.FieldDescriptorProto.TYPE_STRING),
        ('cpu_info', 12, descriptor_pb2.FieldDescriptorProto.TYPE_STRING),
        ('total_ram', 13, descriptor_pb2.FieldDescriptorProto.TYPE_INT32),
        ('gpu_name', 14, descriptor_pb2.FieldDescriptorProto.TYPE_STRING),
        ('gpu_version', 15, descriptor_pb2.FieldDescriptorProto.TYPE_STRING),
        ('user_id', 16, descriptor_pb2.FieldDescriptorProto.TYPE_STRING),
        ('ip_address', 17, descriptor_pb2.FieldDescriptorProto.TYPE_STRING),
        ('language', 18, descriptor_pb2.FieldDescriptorProto.TYPE_STRING),
        ('open_id', 19, descriptor_pb2.FieldDescriptorProto.TYPE_STRING),
        ('access_token', 20, descriptor_pb2.FieldDescriptorProto.TYPE_STRING),
        ('platform_type', 21, descriptor_pb2.FieldDescriptorProto.TYPE_INT32),
        ('field_99', 99, descriptor_pb2.FieldDescriptorProto.TYPE_STRING),
        ('field_100', 100, descriptor_pb2.FieldDescriptorProto.TYPE_STRING),
    ]

    for name, num, ftype in fields:
        f = msg.field.add()
        f.name = name
        f.number = num
        f.label = descriptor_pb2.FieldDescriptorProto.LABEL_OPTIONAL
        f.type = ftype

    pool = descriptor_pool.DescriptorPool()
    pool.Add(file_proto)
    
    try:
        return message_factory.GetMessageClass(pool.FindMessageTypeByName('GameData'))
    except AttributeError:
        factory = message_factory.MessageFactory(pool)
        return factory.GetPrototype(pool.FindMessageTypeByName('GameData'))

GameData = _build_gamedata()