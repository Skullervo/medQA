import grpc
import analyze_all_service_pb2
import analyze_all_service_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50053') as channel:
        stub = analyze_all_service_pb2_grpc.AnalyzeAllServiceStub(channel)
        response = stub.AnalyzeAll(analyze_all_service_pb2.AnalyzeAllRequest())
        print(response.message)

if __name__ == '__main__':
    run()