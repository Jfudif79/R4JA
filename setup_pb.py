# setup_pb.py
import subprocess

my_proto = '''syntax = "proto3";
message GameData {
    string timestamp = 1;
    string game_name = 2;
    int32 game_version = 3;
    string version_code = 4;
    string os_info = 5;
    string device_type = 6;
    string network_provider = 7;
    string connection_type = 8;
    int32 screen_width = 9;
    int32 screen_height = 10;
    string dpi = 11;
    string cpu_info = 12;
    int32 total_ram = 13;
    string gpu_name = 14;
    string gpu_version = 15;
    string user_id = 16;
    string ip_address = 17;
    string language = 18;
    string open_id = 19;
    string access_token = 20;
    int32 platform_type = 21;
    string field_99 = 99;
    string field_100 = 100;
}
'''

out_proto = '''syntax = "proto3";
message Garena_420 {
    string token = 1;
    string field_2 = 2;
    string field_3 = 3;
    string field_4 = 4;
    string field_5 = 5;
    string field_6 = 6;
    string field_7 = 7;
    string field_8 = 8;
    string field_9 = 9;
    string field_10 = 10;
    string field_11 = 11;
    string field_12 = 12;
    string field_13 = 13;
    string field_14 = 14;
    string field_15 = 15;
    string field_16 = 16;
    string field_17 = 17;
    string field_18 = 18;
    string field_19 = 19;
    string field_20 = 20;
    string field_21 = 21;
    string field_22 = 22;
    string field_23 = 23;
    string field_24 = 24;
    string field_25 = 25;
    string field_26 = 26;
    string field_27 = 27;
    string field_28 = 28;
    string field_29 = 29;
    string field_30 = 30;
}
'''

with open("my.proto", "w") as f:
    f.write(my_proto)
with open("output.proto", "w") as f:
    f.write(out_proto)

print("[✔] .proto files written")

subprocess.run(["python", "-m", "grpc_tools.protoc", "-I.", "--python_out=.", "my.proto"], check=True)
subprocess.run(["python", "-m", "grpc_tools.protoc", "-I.", "--python_out=.", "output.proto"], check=True)

print("[✔] my_pb2.py and output_pb2.py generated successfully!")