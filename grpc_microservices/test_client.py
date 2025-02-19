import grpc
import analyze_all_service_pb2
import analyze_all_service_pb2_grpc

channel = grpc.insecure_channel("localhost:50053")
stub = analyze_all_service_pb2_grpc.AnalyzeAllServiceStub(channel)

response = stub.AnalyzeAll(analyze_all_service_pb2.AnalyzeAllRequest())
print(response.message)
