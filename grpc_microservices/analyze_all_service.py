import grpc
from concurrent import futures
import analyze_all_service_pb2
import analyze_all_service_pb2_grpc
import analyze_service_pb2
import analyze_service_pb2_grpc
import requests
import os

ORTHANC_URL = os.getenv("ORTHANC_URL", "http://localhost:8042")

class AnalyzeAllService(analyze_all_service_pb2_grpc.AnalyzeAllServiceServicer):
    def AnalyzeAll(self, request, context):
        try:
            # 🔍 Haetaan kaikki sarjat Orthancista
            response = requests.get(f"{ORTHANC_URL}/series")
            if response.status_code != 200:
                context.set_code(grpc.StatusCode.INTERNAL)
                context.set_details("Failed to fetch series from Orthanc")
                return analyze_all_service_pb2.AnalyzeAllResponse(message="Error fetching series.")

            series_list = response.json()
            print(f"📡 Löytyi {len(series_list)} sarjaa analysoitavaksi.")

            # 🔄 Kutsutaan AnalyzeService:ä jokaiselle sarjalle
            analyze_channel = grpc.insecure_channel("localhost:50052")
            analyze_stub = analyze_service_pb2_grpc.AnalyzeServiceStub(analyze_channel)

            for series_id in series_list:
                print(f"📊 Analysoidaan sarja: {series_id}")
                analyze_response = analyze_stub.AnalyzeDicomData(
                    analyze_service_pb2.AnalyzeRequest(series_id=series_id)
                )
                print(f"✅ {series_id}: {analyze_response.message}")

            return analyze_all_service_pb2.AnalyzeAllResponse(message="Kaikki sarjat on analysoitu!")

        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(str(e))
            return analyze_all_service_pb2.AnalyzeAllResponse(message="Virhe analyysissä.")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    analyze_all_service_pb2_grpc.add_AnalyzeAllServiceServicer_to_server(AnalyzeAllService(), server)
    server.add_insecure_port("[::]:50053")
    server.start()
    print("🚀 Analyze All Service käynnistetty (portti 50053)")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
