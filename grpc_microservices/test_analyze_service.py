"""
TEST CODE FOR ANALYZE SERVICE --> Analyzes all series from Orthanc and send analysis results to DB 
"""


import grpc
import analyze_service_pb2
import analyze_service_pb2_grpc

channel = grpc.insecure_channel("localhost:50052")
stub = analyze_service_pb2_grpc.AnalyzeServiceStub(channel)

print("📡 Requesting analysis for all series in Orthanc")
response = stub.AnalyzeAllDicomData(analyze_service_pb2.AnalyzeAllRequest())

print(f"✅ Response: {response.message}")
